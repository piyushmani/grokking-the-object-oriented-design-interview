from dataclasses import dataclass, field
import datetime
from shipment.shipment_log import ShipmentLog

@dataclass
class Shipment:
    shipment_number: int
    shipment_method: str
    shipment_date: datetime.date = datetime.date.today()
    estimated_arrival: datetime.date = datetime.date.today()
    shipment_logs: list = field(default_factory=list)

    def add_shipment_log(self, shipment_log: ShipmentLog):
        self.shipment_logs.append(shipment_log)
