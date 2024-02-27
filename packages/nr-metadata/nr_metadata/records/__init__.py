from oarepo_runtime.records.systemfields import PathSelector


class PeopleSelector(PathSelector):
    def __init__(self):
        super().__init__("metadata.creators", "metadata.contributors")

    def select(self, record):
        ret = set()
        for rec in super().select(record):
            if rec.get("type") == "personal":
                full_name = rec.get("fullName")
                if full_name:
                    ret.add(full_name)
        return list[ret]
