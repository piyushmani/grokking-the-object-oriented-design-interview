from dataclasses import dataclass
import datetime
from enum import Enum

class ShipmentStatus(Enum):
    PENDING, SHIPPED, DELIVERED, ON_HOLD = 1, 2, 3, 4

@dataclass
class ShipmentLog:
    shipment_number: int
    status: ShipmentStatus = ShipmentStatus.PENDING
    creation_date: datetime.date = datetime.date.today()
