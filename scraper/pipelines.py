
class DuplicatesPipeline(object):

    def process_item(self, item, spider):
        # Removes duplicates (roughly)
        item["emails"] = list(set(item["emails"]))
        return item
