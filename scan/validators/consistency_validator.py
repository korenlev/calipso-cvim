from scan.validators.validator_base import ValidatorBase


class ConsistencyValidator(ValidatorBase):
    def run(self, save_result: bool = False) -> (bool, list):
        errors = []
        objects_list = self.inv.find(search={"environment": self.env},
                                     projection=['_id', 'id'])

        object_ids = [o['id'] for o in objects_list]
        object_db_ids = [str(o['_id']) for o in objects_list]

        links = self.inv.find(collection="links",
                              search={"environment": self.env},
                              projection=["_id", "source", "source_id", "target", "target_id"])

        link_ids = []
        for link in links:
            link_ids.append(str(link["_id"]))

            missing_ids = []
            for field in ('source', 'target'):
                if str(link[field]) not in object_db_ids:
                    missing_ids.append((field, link[field]))

                id_field = "{}_id".format(field)
                if link[id_field] not in object_ids:
                    missing_ids.append((id_field, link[id_field]))

            if missing_ids:
                errors.append("Link '{}' has missing ids ::: {}".format(link["_id"],
                                                                        ";".join("{}: {}".format(m[0], m[1])
                                                                                 for m in missing_ids)))

        cliques = self.inv.find(collection="cliques",
                                search={"environment": self.env},
                                projection=["_id", "focal_point", "focal_point_object_id", "nodes", "links"])

        for clique in cliques:
            missing_ids = []

            if str(clique["focal_point"]) not in object_db_ids:
                missing_ids.append(("focal_point", clique["focal_point"]))
            if clique["focal_point_object_id"] not in object_ids:
                missing_ids.append(("focal_point_object_id", clique["focal_point_object_id"]))

            missing_nodes = [str(node_id) for node_id in clique["nodes"] if str(node_id) not in object_db_ids]
            if missing_nodes:
                missing_ids.append(("nodes", ",".join(missing_nodes)))
            missing_links = [str(link_id) for link_id in clique["links"] if str(link_id) not in link_ids]
            if missing_links:
                missing_ids.append(("links", ",".join(missing_links)))

            if missing_ids:
                errors.append("Clique '{}' has missing ids ::: {}".format(clique["_id"],
                                                                          ";".join("{}: {}".format(m[0], m[1])
                                                                                   for m in missing_ids)))

        return self.process_result(errors=errors, save_to_db=save_result)
