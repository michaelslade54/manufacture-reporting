from openupgradelib import openupgrade

xml_ids = ["bom_structure_xlsx"]

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.delete_records_safely_by_xml_id(env, xml_ids)