import os
import census20xx

print(census20xx.all_data['AK']['Anchorage'])
#print(census20xx.all_data['AK'])

anchorage_pop = census20xx.all_data['AK']['Anchorage']['pop']
print('В 20xx году численность населения округа Anchorage составляла ' + str(anchorage_pop))
