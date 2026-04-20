
from .user import *
from .vehicle import *
from .vehicle_log import *
from .country import *
from .city import *
from .company import *
from .shipment import *

admin.site.register(Vehicle)
admin.site.register(VehicleLog)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Shipment)