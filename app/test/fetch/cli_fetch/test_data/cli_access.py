COMPUTE_HOST_ID = "node-5.cisco.com"
COMMAND = "virsh list"
CACHED_COMMAND = "ssh -o StrictHostKeyChecking=no " + COMPUTE_HOST_ID + " sudo " + COMMAND

RUN_RESULT = " Id    Name                           State\n----------------------------------------------------\n 2     instance-00000002              running\n 27    instance-0000001c              running\n 38    instance-00000026              running"

LINES_FOR_FIX = [
    "br-ex\t\t8000.005056acc9a2\tno\t\teno33554952",
    "\t\t\t\t\t\t\tp_ff798dba-0",
    "\t\t\t\t\t\t\tv_public",
    "\t\t\t\t\t\t\tv_vrouter_pub",
    "br-fw-admin\t\t8000.005056ace897\tno\t\teno16777728",
    "br-mesh\t\t8000.005056acc9a2\tno\t\teno33554952.103",
    "br-mgmt\t\t8000.005056ace897\tno\t\teno16777728.101",
    "\t\t\t\t\t\t\tmgmt-conntrd",
    "\t\t\t\t\t\t\tv_management",
    "\t\t\t\t\t\t\tv_vrouter",
    "br-storage\t\t8000.005056ace897\tno\t\teno16777728.102"
]

FIXED_LINES = [
    "br-ex\t\t8000.005056acc9a2\tno\t\teno33554952,p_ff798dba-0,v_public,v_vrouter_pub",
    "br-fw-admin\t\t8000.005056ace897\tno\t\teno16777728",
    "br-mesh\t\t8000.005056acc9a2\tno\t\teno33554952.103",
    "br-mgmt\t\t8000.005056ace897\tno\t\teno16777728.101,mgmt-conntrd,v_management,v_vrouter",
    "br-storage\t\t8000.005056ace897\tno\t\teno16777728.102"
]

LINE_FOR_PARSE = "br-ex\t\t8000.005056acc9a2\tno\t\teno33554952,p_ff798dba-0,v_public,v_vrouter_pub"
PARSED_LINE = {
    "bridge_id": "8000.005056acc9a2",
    "bridge_name": "br-ex",
    "interfaces": "eno33554952,p_ff798dba-0,v_public,v_vrouter_pub",
    "stp_enabled": "no"
}
HEADERS = ["bridge_name", "bridge_id", "stp_enabled", "interfaces"]
