#Name: Phat Vo
#PSID: 2024127
#Lab10.11
class FoodItem:
    def __init__(self, name='None', fat=0.00, carbs=0.00,protein=0.00):
        self.name=name
        self.fat=fat
        self.carbs=carbs
        self.protein=protein


    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
if __name__=='__main__':
    food1=FoodItem()
    name= input()
    fat=float(input())
    carbs=float(input())
    protein=float(input())
    num_serving=float(input())

    food2= FoodItem(name,fat,carbs,protein)
    calories0 = food1.get_calories(num_serving)
    calories = food2.get_calories(num_serving)

    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_serving,calories0))
    print()
    food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_serving,calories))