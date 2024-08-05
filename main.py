class TicketResesrvationSystem:

    def __init__(self, total_tickets):

      self.total_tickets = total_tickets 
      self.reservations = {} 


    def display_status(self): 
       
       reserved_tickets = sum(self.reservation.values())

       print(f"Total tickets: {self.total_tickets}")
       print(f"Reserved tickets : {reserved_tickets}")

       print(f"Available tickets: {self.total_tickets - reserved_tickets}")


    def display_reservation(self):

       if not self.reservation:

           print("No reservation made yet")

       else: 

             print("Current reservation:")  

             for user, tickets in self.reservation.items():
                 
                print(f"User: {user}, Tickets: {tickets}")


    def reserve_ticket(self, user, ticket): 

        if ticket <= 0:

            print("Invalid number of tickets to reserve.")

        elif sum(self.reservation.values()) + tickets > self.total_tickets: 

            print("Not enough avialable tickets in reserve.") 

        else: 

             if user in self.reservation:

                 self.reservation[user] += tickets 

             else: 

                 self.reservation[user] = tickets 

             print(f"{tickets} ticket(s) reserved successfully for {user}")



    def cancel_reservation(self, user, tickets):

        if user not in self.reservations: 

            print(f"No reservation found for user: {user}")


        elif tickets <= 0:

            print("Invalid number of tickets to cancel.")


        elif tickets > self.reservations[user]:

            print("You dont't have that many tickets reserved.") 


        else:

            self.reservations[user] -= tickets

            if self.reservations[user] == 0:

                del self.reservations[user]

            print(f"{tickets} tickets(S) reservation canceled successfully for {user}") 


    def search_reservation(self, user):

        if user in self.reservations:

            print(f"User: {user}, Tickets: {self.reservations[user]}")

        else:

            print(f"No reservation found for user: {user}") 



def main():

    system = TicketResesrvationSystem(total_tickets=10)


    while True:

        print("\n1. Display ticket status")
        print("2. Display all reservations")
        print("3. Reserve tickets")
        print("4. Cancel reservation")
        print("5. Search reservation by user")
        print("6. Exit")


        choice = input("Enter your choice: ")  


        if choice == "1": 

            system.display_status()


        elif choice == "2":

            system.display_reservation()


        elif choice == "3": 

            user = input("Enter your name: ")

            tickets = int(input("Enter number of tickets to reserve: ")) 

            system.reserve_ticket(user, tickets)

        elif choice == "4": 

            user = input("Enter your name: ")


            tickets = int(input("Enter number of ticket to cancel: "))

            system.cancel_reservation(user, tickets)


        elif choice == "5":

            user = input("Enter the name to search: ")

            system.search_reservation(user)

        elif choice == "6":

            print("Exiting the System.")
            break 

        else:

            print("Invalid choice. Please try again")




if __name__=="__main__"

    main()  