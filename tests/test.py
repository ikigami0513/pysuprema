from suprema.biostar2 import *

biostar2 = Biostar2(
    server_ip="https://suprema-api.biostar2.com",
    login_id="test-api",
    password="Suprema2023!"
)

name = "Groupe Test"
print(biostar2.endpoint(UserGroup).create(name))
print(biostar2.endpoint(UserGroup).get(name))
print(biostar2.endpoint(UserGroup).delete(name))