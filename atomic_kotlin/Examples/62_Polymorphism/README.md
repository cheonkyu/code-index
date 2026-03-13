# 62. Polymorphism (다형성)

안녕하세요, 초보자 여러분! 오늘은 프로그래밍에서 정말 중요한 개념 중 하나인 **다형성 (Polymorphism)**에 대해 배워볼게요. 다형성이란 그리스어로 "많은 형태"를 의미하는데, 프로그래밍에서는 **같은 인터페이스나 메서드가 여러 가지 형태로 동작할 수 있다는 뜻**이에요. 쉽게 말해, 같은 이름의 함수나 메서드가 다양한 상황에 따라 다르게 작동할 수 있다는 거죠!

## 기본 개념 이해하기

### 예제 1: `Pet` 클래스 예시

우선 간단한 `Pet` 클래스를 통해 다형성을 이해해볼게요.

```kotlin
package polymorphism
import atomictest.eq

// 기본 `Pet` 클래스 정의
open class Pet {
    open fun speak() = "Pet"  // 모든 펫은 기본적으로 "Pet"라고 말해요
}

// 하위 클래스 `Dog`와 `Cat` 정의
class Dog : Pet() {
    override fun speak() = "Bark!"  // 개는 "Bark!"라고 말해요
}

class Cat : Pet() {
    override fun speak() = "Meow"  // 고양이는 "Meow"라고 말해요
}

// `speak` 메서드를 호출하는 함수
fun talk(pet: Pet) {
    println(pet.speak())
}

fun main() {
    talk(Dog())  // 출력: Bark!
    talk(Cat())  // 출력: Meow
}
```

**간단 설명:**
- `Pet` 클래스는 모든 펫이 공유하는 기본 메서드 `speak()`을 정의해요.
- `Dog`와 `Cat` 클래스는 `speak()` 메서드를 각각 자신만의 방식으로 오버라이드해요.
- `talk()` 함수는 `Pet` 타입의 객체를 받아서 `speak()` 메서드를 호출해요. 하지만 실제 객체는 `Dog`나 `Cat`일 수 있어요.
- **핵심 포인트:** `talk()` 함수는 객체의 실제 타입(`Dog` 또는 `Cat`)을 알지만, `speak()` 메서드 호출 시에는 해당 객체의 오버라이드된 메서드가 실행되는 거예요. 이렇게 실행 시점에 맞는 메서드가 호출되는 것을 **동적 바인딩 (Dynamic Binding)** 또는 **런타임 다형성**이라고 해요.

### 예제 2: `Character` 인터페이스 예시

다음으로 좀 더 복잡한 예제를 통해 다형성의 또 다른 측면을 살펴볼게요.

```kotlin
package polymorphism
import atomictest.*

// 추상 클래스 `Character` 정의
abstract class Character(val name: String) {
    abstract fun play(): String  // 캐릭터가 할 수 있는 동작 정의
}

// 인터페이스 `Fighter`와 `Magician` 정의
interface Fighter {
    fun fight() = "Fight!"
}

interface Magician {
    fun doMagic() = "Magic!"
}

// 하위 클래스 `Warrior`, `Elf`, `FightingElf` 정의
class Warrior : Character("Warrior"), Fighter {
    override fun play() = fight()  // 전사는 싸우는 동작을 해요
}

open class Elf(name: String = "Elf") : Character(name), Magician {
    override fun play() = doMagic()  // 엘프는 마법을 사용해요
}

class FightingElf : Elf("FightingElf"), Fighter {
    override fun play() = super.play() + fight()  // 엘프가 싸우는 동작도 추가
}

// 확장 함수 `playTurn()` 정의
fun Character.playTurn() {
    println("${name}: ${play()}")  // 캐릭터 이름과 동작 출력
}

fun main() {
    val characters: List<Character> = listOf(
        Warrior(), Elf(), FightingElf()
    )
    characters.forEach { it.playTurn() }
    // 출력 예상:
    // Warrior: Fight!
    // Elf: Magic!
    // FightingElf: Magic!Fight!
}
```

**간단 설명:**
- `Character` 클래스는 추상 클래스로, 하위 클래스들이 각자의 동작을 정의하게 돼요.
- `Warrior`와 `Elf`는 각각 `fight()`와 `doMagic()`을 실행해요.
- `FightingElf`는 두 동작을 모두 수행해요.
- `playTurn()` 함수는 `Character` 타입의 객체에 대해 확장 함수로 정의되어 있어요. 이 함수는 **정적 바인딩**으로 작동해요. 즉, 컴파일 시점에 정확히 어떤 동작을 할지 결정되지만, `play()` 호출 시에는 객체의 실제 타입에 따라 동작이 달라져요. 이를 **동적 바인딩**이라고 해요.

## 주요 핵심 개념 요약

1. **다형성의 목적**: 같은 이름의 메서드가 다양한 타입의 객체에 따라 다르게 동작하게 만드는 거예요.
2. **업캐스팅 (Upcasting)**: 하위 타입의 객체를 상위 타입으로 취급하는 것. 예를 들어, `Dog`나 `Cat`을 `Pet` 타입으로 취급해요.
3. **동적 바인딩 (Dynamic Binding)**: 메서드 호출 시점에 실제 객체 타입에 따라 적절한 메서드가 실행되는 메커니즘이에요. 이는 런타임에 결정되므로 유연성을 제공해요.

이렇게 다형성을 이해하면 코드의 유연성과 재사용성이 크게 향상되는데요, 다양한 상황에서 일관된 동작을 보장하면서도 코드를 간결하게 유지할 수 있어요. 연습을 통해 더 익숙해지길 바랄게요! 질문이 있으면 언제든지 물어보세요. 😊