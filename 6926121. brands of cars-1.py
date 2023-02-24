#https://github.com/Francisakrofi/Francis-Akrofi/issues  
#brands of cars with their prices
#brands of Nissan, Toyota, Mercedes, Honda
#prices of cars in Ghana cedis
cars = {
'Honda accord': 27300,
'Honda civic':28000,
'Honda HR-V':32000,
'Honda passport':41100,
'Honda pilot':39150,
'Toyota camry':3250,
'Toyota landcruiser':57230,
'Toyota tacoma':35700,
'Toyota sienna':31200,
'Toyota highlander':39500,
'Toyota hilux':37400,
'Toyota yaris':21900,
'Toyota tundra':41200,
' Mercedes-Benz E-Class':71200,
'Mercedes-Benz A Class':69210,
'Mercedes-Benz GLA':65920,
'Mercedes-BenzGLB':62900,
'Mercedes-Benz Citan':67300,
'Mercedes-Benz AMG':53480,
'Mercedes-Benz EQS':51200,
'Nissan ariya':92340,
'Nissan leaf':92340,
'Nissan note':81340,
'Nissan serena':52190,
'Nissan march':52800,
'Nissan altima':42710,
'Nissan cima':45800,
'Nissan sentra':49350,
'Nissan qashqai':35620,
'Nissan terrano':32560,
}
car_name=input('Specify car type: ') 
if car_name in cars:
    print(f'the price of {car_name} is {cars[car_name]:,} cedis ')
else:
    print(f'oops {car_name} is not available.Try other brands.eg:Toyota, Nissan, Honda')   