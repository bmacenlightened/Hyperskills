package machine
import java.lang.Integer.min
import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)
    var machine = CoffeeMaker(400, 540, 120, 9, 550)
    var action = ""
    while (true) {
        println("\nWrite action (buy, fill, take, remaining, exit):")
        action = scanner.nextLine()
        if (action == "buy") {
            println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            var buy = scanner.nextLine()
            when (buy) {
                "1" -> {
                    machine.buyEspresso()
                }
                "2" -> {
                    machine.buyLatte()
                }
                "3" -> {
                    machine.buyCappuccino()
                }
                "back" -> {

                }
            }
            println("")
        } else if (action == "fill") {
            println("Write how many ml of water do you want to add:")
            var newWater = scanner.nextInt()
            println("Write how many ml of milk do you want to add:")
            var newMilk = scanner.nextInt()
            println("Write how many grams of coffee beans do you want to add:")
            var newBeans = scanner.nextInt()
            println("Write how many disposable cups of coffee do you want to add:")
            var newCups = scanner.nextInt()
            machine.fill(newWater, newMilk, newBeans, newCups)
            println("")
        } else if (action == "take") {
            machine.take()
            println("")
        } else if (action == "remaining") {
            println("")
            machine.displayMachine()
        } else if (action == "exit") {
            break;
        }
    }
}

class CoffeeMaker(var water: Int, var milk: Int, var beans: Int, var cups: Int, var money: Int) {

    fun displayMachine() {
        println("The coffee machine has:")
        println("$water of water")
        println("$milk of milk")
        println("$beans of coffee beans")
        println("$cups of disposable cups")
        println("$money of money")
    }

    fun take() {
        println("I gave you $${money}")
        money = 0
    }

    fun fill(newwater: Int, newmilk: Int, newbeans: Int, newcups: Int) {
        water += newwater
        milk += newmilk
        beans += newbeans
        cups += newcups
    }

    fun buyEspresso() {
        if (water >= 250 && beans >= 16 && cups >= 1) {
            println("I have enough resources, making you a coffee!")
            water -= 250
            beans -= 16
            money += 4
            cups -= 1
        } else if (water < 250) {
            println("Sorry, not enough water!")
        } else if (beans < 16) {
            println("Sorry, not enough beans!")
        } else {
            println("Sorry, not enough cups!")
        }
    }

    fun buyLatte() {
        if (water >= 350 && milk >= 75 && beans >= 20 && cups >= 1) {
            println("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            cups -= 1
        } else if (water < 350) {
            println("Sorry, not enough water!")
        } else if (milk < 75) {
            println("Sorry, not enough milk!")
        } else if (beans < 20){
            println("Sorry, not enough beans!")
        } else {
            println("Sorry, not enough cups!")
        }
    }

    fun buyCappuccino() {
        if (water >= 200 && milk >= 100 && beans >= 12 && cups >= 1) {
            println("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            cups -= 1
        } else if (water < 200) {
            println("Sorry, not enough water!")
        } else if (milk < 100 ) {
            println("Sorry, not enough milk!")
        } else if (beans < 12) {
            println("Sorry, not enough beans!")
        } else {
            println("Sorry, not enough cups!")
        }
    }
}