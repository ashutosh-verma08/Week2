# Programmer - Ashu tosh Verma( astverma@)
# Dated: 03-27-2025

# To calculate the bonus a receiver gets
# Input - Number of days worked

# Slabs of bonus in program
#days <= 32  Bonus = 0
#days > 32 and days <= 40 Bonus = (( days - 32 ) * 325) + Bonus
#days > 40 and days <= 48 Bonus = (( days - 40) * 550) + Bonus
#days > 48 Bonus = ((Days - 48) *600) + Bonus

# Input the number of days worked
days = int(input("Enter days: "))

# Variable section
bonus = 0

# Main Code

if (days <= 32):
    bonus = 0

elif(days > 32 and days <= 40):
    bonus = (days - 32  ) * 325 

elif(days > 40 and days <= 48):
    bonus = ((days - 40) * 550) + ( 8 * 325)

elif(days > 48):
    bonus = ((days - 48) * 600) + (8 * 550) + (8 * 325)

# Output section 
print("Bonus for" , days,"days is USD" , bonus )
