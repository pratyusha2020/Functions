class Vehicle:
    def __init__(self,name,sc,mc):
        self.name= name
        self.seating_capacity= sc
        self.maint_cost= mc
    
        
class Bus(Vehicle):
 pass


bus= Bus("Tata Motors", 50,'10% of seating capacity*100')

Bus_Fare= (50*100) + ((50*100)*0.1)

print("Vehicle Name:",bus.name,"\nSeating Capacity:",
bus.seating_capacity, "\nMaintanence Cost:",bus.maint_cost)
print("Total bus fare(in rupees):", Bus_Fare)