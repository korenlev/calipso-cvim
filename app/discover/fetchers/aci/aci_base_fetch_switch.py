from discover.fetchers.aci.aci_access import AciAccess


class AciBaseFetchSwitch(AciAccess):

    def fetch_pnic_interface(self, switch_id, pnic_id):
        dn = "/".join((switch_id, "sys", "phys-[{}]".format(pnic_id)))
        response = self.fetch_mo_data(dn)
        interface_data = self.get_objects_by_field_names(response, "l1PhysIf",
                                                                   "attributes")
        return interface_data[0] if interface_data else None
