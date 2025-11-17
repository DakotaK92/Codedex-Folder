const departTripTicket = {
  name: "Dakota",
  from: "Orlando, Florida",
  to: "Dallas, Texas",
  businessClass: false,
  upgrade () {
    if(this.businessClass) {
      console.log("Your ticket is already business class!")
    } else {
      this.buinessClass = true;
      console.log("Ticket upgraded to business class!")
    }
  },
}

const returnTripTicket = {
  name: "Dakota",
  from: "Dallas, Texas",
  to: "Orlando, Florida",
  businessClass: true,
  upgrade () {
    if(this.businessClass) {
      console.log("Your ticket is already business class!")
    } else {
      this.businessClass = true;
      console.log("Ticket upgraded to business class!")
    }
  },
}

departTripTicket.upgrade();
returnTripTicket.upgrade();