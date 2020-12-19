keys=["Roll", "Regd", "Name", "Branch", "Stream", "Sem", "Phone", "Address"]
details = {k: input("Please enter your {}: ".format(k)) for k in keys}

print("My name is {}. I am from {}. Currently I am in Sem-{} of {} - {}. My roll no is {} and registration number is {}. To know more, call {}."
.format(details["Name"], details["Address"], details["Sem"], details["Stream"], details["Branch"], details["Roll"], details["Regd"], details["Phone"]))