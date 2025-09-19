
# global requisition_counter
requisition_counter = 10001# It ensures that every new requisition gets a unique ID by starting from 10001 and increasing by 1 each time.


class Requisitionsystem:#The Requisitionsystem class represents a blueprint for creating requisition objects.
    
    whole_requisitions = []
    #This is xxx a class-level list. It stores all requisitions ever created.
    
    
    def __init__(self):
        # runs automatically when you create a new requisition object. It initializes the attributes of each requisition. 
        global requisition_counter
        self.requisition_id = requisition_counter
        #self means this particular object. Each requisition has its own data stored separately.
        self.total_cost = 0
        self.status = "New"
        self.reference_number = None
        requisition_counter +=1

        self.date = input("Enter date (DD/MM/YYYY): ")
        self.staff_id = input("Enter Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")

        # global collection
        Requisitionsystem.whole_requisitions.append(self)
        #This saves the requisition object into the shared list of all requisitions.

    def requisitions_details(self):
        #This method asks for item names and costs, then calculates the total cost.
        number = int(input("How many items to add? "))
        total = 0
        for i in range(number):
            item_name = input(" Please enter the item : ")
            cost = int(input("Enter cost of item : "))
            total += cost
        self.total_cost = total
        print(f"Total price: ${self.total_cost}") 




    def requisition_approval(self):
            if self.total_cost <= 500:#    # K.I.S.S applied: Simple if-else logic for automatic approval
                #This is decision making. Business rule: requisitions under $500 are auto-approved, others need review.
                self.status = "Approved"
                self.reference_number = self.staff_id + str(self.requisition_id)[-3:]
            else:
                self.status = "Pending"
                self.reference_number = None
                print(f"Status: {self.status}")





    #  response for pending requisition
    def respond_requisition(self):
        #Manager intervention. If cost is high, the manager decides manually. weather he want to approved or not.
        if self.status == "Pending":
            decision = input("Manager: Approve or Not Approved? ").strip()
            if decision in ["Approved", "Not Approved"]:
                self.status = decision
                print(f"Updated Status: {self.status}")
            else:
                print("Invalid input. Status unchanged.")  

    # Display 
    def display_requisition(self):
        #Output presentation. Shows all details of the requisition clearly.
        print("\n  Requisition information  ")
        print(f"Date: {self.date}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Total Cost: ${self.total_cost}")
        print(f"Reference Number: {self.reference_number}")
        print(f"Status: {self.status}")

    def requisition_statistic(self):
        #This function counts how many requisitions there are in total, and how many are Approved, Pending, or Not Approved.

        total_requistion=len(Requisitionsystem.whole_requisitions)#length
        approved= sum(
            1 for requisition in Requisitionsystem.whole_requisitions
            if requisition.status == "Approved")
        pending = sum(
            1 for requisition in Requisitionsystem.whole_requisitions
            if requisition.status == "Pending")
        notApproved = sum(
            1 for requisition in Requisitionsystem.whole_requisitions 
                if requisition.status == "Not Approved")
        
        print("\n Total Requisition")
        print(f"Total Requisition:{total_requistion}")
        print(f"Approved: {approved}")
        print(f"Pending: {pending}")
        print(f"NOt Approved: {notApproved}")

number_requisitions= int(input("How many requisitions do you want ?: "))
#Allows handling more than one requisition at once.
for i in range(number_requisitions):
    print("\n   Printing Requisition  ")
    requisition = Requisitionsystem()
    requisition.requisitions_details()
    requisition.requisition_approval()
    requisition.respond_requisition()
    requisition.display_requisition()

if Requisitionsystem.whole_requisitions:
    #This checks if there are any requisitions before showing statistics.
    Requisitionsystem.whole_requisitions[0].requisition_statistic()
else:
    print("No requisitions were created.")





