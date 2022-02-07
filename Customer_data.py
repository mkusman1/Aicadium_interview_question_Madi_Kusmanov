from pydantic import BaseModel
# Create Class which describes customer data measurements to be
# used for prediciton in API
class Customer_id(BaseModel):
    BounceRates: float 
    ExitRates: float 
    PageValues: float	
    SpecialDay: float
    Month: float
    OperatingSystems: int
    Browser: int
    Region: int
    TrafficType: int
    VisitorType: int
    Weekend: int
    ProductRelated_rate: float
    Administrative_rate: float
    Informational_rate: float