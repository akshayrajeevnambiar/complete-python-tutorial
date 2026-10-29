# Coffee Machine Project - Build Checklist

## Core Features

### 1. Menu & Drink Selection
- [ ] Define drinks available (espresso, latte, cappuccino) with recipes and prices
- [ ] Prompt user: "What would you like? (espresso/latte/cappuccino):"
- [ ] Validate user input (must be valid drink or special command)
- [ ] Prompt repeats after each action completes

### 2. Machine Control
- [ ] User can enter "off" to turn off the machine and end execution
- [ ] User can enter "report" to see current resources

### 3. Report Generation
- [ ] Display Water (ml), Milk (ml), Coffee (g), Money ($)
- [ ] Only accessible via "report" command

### 4. Resource Management
- [ ] Track: water, milk, coffee, money in the machine
- [ ] Initial values: water=300ml, milk=200ml, coffee=100g, money=$0
- [ ] Check if resources are sufficient for selected drink
- [ ] Print error message if any resource is insufficient (water, milk, or coffee)
- [ ] Deduct resources after successful purchase

### 5. Coin Processing
- [ ] Prompt for coins: quarters ($0.25), dimes ($0.10), nickels ($0.05), pennies ($0.01)
- [ ] Calculate total monetary value from coin counts
- [ ] Only prompt for coins if resources are sufficient

### 6. Transaction Validation
- [ ] Check if coins inserted >= drink cost
- [ ] If insufficient: print "Sorry that's not enough money. Money refunded."
- [ ] If sufficient: add drink cost to machine money
- [ ] If overpaid: calculate change and print "Here is ${change} in change."
- [ ] Round change to 2 decimal places

### 7. Dispensing
- [ ] After successful payment, deduct ingredients from resources
- [ ] Print: "Here is your {drink}. Enjoy!"
- [ ] Return to menu prompt for next customer

## Build Order (Recommended)
1. Set up data structures for drinks and resources
2. Create main loop that prompts for user input
3. Implement "off" and "report" commands
4. Build drink selection and resource checking
5. Add coin collection and transaction logic
6. Complete the full game loop with prompting

## Example Flow
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.00 in change.
Here is your latte. Enjoy!
What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
What would you like? (espresso/latte/cappuccino): off
```
