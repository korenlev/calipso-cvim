import abc

from base.utils.inventory_mgr import InventoryMgr


class ValidatorBase(metaclass=abc.ABCMeta):
    COLLECTION = "validations"

    def __init__(self, env):
        self.env = env
        self.inv = InventoryMgr()

    @abc.abstractmethod
    def run(self, save_result: bool = False) -> (bool, list):
        """
        Runs code-defined validations based on DB data.

        Arguments:
        save_result - defines whether the validation results should be saved to db

        Returns validation result (successful or not) and the list of found errors
        """
        return True, []

    def process_result(self, errors: list, save_to_db: bool):
        result = not errors
        if save_to_db:
            self.save_result(result, errors)
        return result, errors

    def save_result(self, run_result: bool, errors: list):
        env_doc = self.inv.find_one({"environment": self.env}, collection=self.COLLECTION)
        if not env_doc:
            env_doc = {
                "environment": self.env,
                "validations": {}
            }

        env_doc["validations"][self.__class__.__name__] = {
            "result": run_result,
            "errors": errors
        }
        self.inv.set(item=env_doc, collection=self.COLLECTION, allow_new_docs=True)
