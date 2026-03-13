# 71. InnerClasses: 내부 클래스 이해하기

안녕하세요! 코틀린 프로그래밍을 처음 접하는 분들을 위해 내부 클래스(Inner Classes)에 대해 쉽게 설명해드릴게요. 내부 클래스는 외부 클래스 안에 정의되는 클래스라고 생각하시면 돼요. 중요한 점은 내부 클래스가 외부 클래스에 대한 참조를 가지고 있다는 거예요. 쉽게 말해, 내부 클래스는 "큰 부모 클래스"에 속해 있다고 보면 돼요.

## 기본 개념 요약

1. **참조 유지**: 내부 클래스 객체는 외부 클래스 객체에 대한 참조를 항상 유지해요. 그래서 외부 클래스의 멤버에 쉽게 접근할 수 있어요.
2. **생성 순서**: 내부 클래스 객체를 생성하려면 반드시 외부 클래스 객체가 먼저 필요해요. 외부 클래스 없이 내부 클래스 객체를 만들 수는 없어요.
3. **명확한 구분**: 내부 클래스에서 `this` 키워드를 사용할 때, 어떤 클래스 객체를 가리키는지 명확히 구분해야 해요. 이때 `this@외부클래스명`으로 구분해요.

## 예제 코드 살펴보기

### 예제: `Hotel` 클래스와 `Room`, `Closet` 내부 클래스

```kotlin
package innerclasses
import atomictest.eq

class Hotel(private val reception: String) { // 외부 클래스: 호텔
    open inner class Room(val id: Int = 0) { // 내부 클래스: 룸
        // 외부 클래스의 'reception' 멤버에 접근 가능
        fun callReception(): String {
            return "Room $id Calling $reception"
        }
    }

    private inner class Closet : Room() { // 또 다른 내부 클래스: 옷장
        // 외부 클래스의 'reception' 멤버에 접근 가능
        override fun callReception(): String {
            return "Room 0 Calling $reception" // 클로에 자체는 id가 없으므로 기본값 사용
        }

        fun callClosetReception(): String {
            return "Closet Calling $reception"
        }
    }

    fun closet(): Closet { // 옷장 객체 생성 함수
        return Closet()
    }
}

fun main() {
    val nycHotel = Hotel("311") // 호텔 객체 생성
    val room = nycHotel.Room(319) // 외부 클래스 객체가 필요함
    println(room.callReception()) eq "Room 319 Calling 311" // 출력: Room 319 Calling 311

    val sfHotel = Hotel("0") // 다른 호텔 객체 생성
    val closet = sfHotel.closet() // 옷장 객체 생성
    println(closet.callReception()) eq "Room 0 Calling 0" // 출력: Room 0 Calling 0
}
```

### 예제: `this` 키워드와 관련된 명확한 구분

```kotlin
package innerclasses
import atomictest.eq
import typechecking.name

class Fruit { // 외부 클래스: 과일
    fun changeColor(color: String) = "Fruit $color"
    fun absorbWater(amount: Int) {}

    inner class Seed { // 내부 클래스: 씨앗
        fun changeColor(color: String) = "Seed $color"
        fun germinate() {}
        
        fun whichThis() {
            // 기본적으로 현재 클래스를 가리킴
            this.name eq "Seed" // 출력: Seed
            // 명시적으로 구분하기 위해 사용
            this@Seed.name eq "Seed" // 출력: Seed
            this@Fruit.name eq "Fruit" // 출력: Fruit
        }

        inner class DNA { // 내부 클래스: DNA
            fun changeColor(color: String) {
                // 재귀적으로 외부와 내부 클래스 접근
                this@Seed.changeColor(color) // Seed 클래스의 changeColor 호출
                this@Fruit.changeColor(color) // Fruit 클래스의 changeColor 호출
            }

            fun plant() {
                // 외부 클래스의 함수 호출 가능
                germinate() // Seed 클래스의 germinate 호출
                absorbWater(10) // Fruit 클래스의 absorbWater 호출
            }
        }
    }
}

// 확장 함수 예시
fun Int.grow() { // 확장 함수: 정수에 대한 grow 함수
    this.name eq "Int" // 기본적으로 호출 주체인 정수 객체를 가리킴
    this@grow.name eq "Int" // 명시적으로 정수 객체를 가리킴
    this@DNA.name eq "DNA" // 내부 클래스 DNA에서 정수 객체 접근
    this@Seed.name eq "Seed" // 씨앗 클래스에서 정수 객체 접근
    this@Fruit.name eq "Fruit" // 과일 클래스에서 정수 객체 접근
}

fun Seed.plant() {} // 씨앗 클래스의 plant 함수
fun Fruit.plant() {} // 과일 클래스의 plant 함수

fun whichThis() {
    // 기본적으로 현재 클래스를 가리킴
    this.name eq "DNA" // 출력: DNA
    // 명시적으로 구분해야 함
    this@DNA.name eq "DNA" // 출력: DNA
    this@Seed.name eq "Seed" // 출력: Seed
    this@Fruit.name eq "Fruit" // 출력: Fruit
}

fun main() {
    val fruit = Fruit()
    fruit.changeColor("Red") eq "Fruit Red" // Fruit 클래스의 changeColor 호출
    val seed = fruit.Seed()
    seed.changeColor("Green") eq "Seed Green" // Seed 클래스의 changeColor 호출
    seed.whichThis() // 출력: Seed
}
```

## 초보자를 위한 팁

- **외부 클래스 객체 필요**: 내부 클래스 객체를 만들 때는 반드시 외부 클래스 객체가 먼저 필요해요.
- **명확한 참조 구분**: `this@외부클래스명`을 사용해 내부 클래스와 외부 클래스 사이의 구분을 명확히 하세요.
- **확장 함수 활용**: 외부 클래스와 내부 클래스 간에 공통 기능을 쉽게 공유할 수 있어요.

이렇게 내부 클래스를 이해하면 코틀린 프로그래밍에서 클래스 간 관계를 좀 더 유연하게 다룰 수 있어요. 질문 있으시면 언제든지 물어보세요! 😊