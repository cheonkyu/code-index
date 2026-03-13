# 19. Constructors

안녕하세요! 코틀린 프로그래밍을 처음 시작하시는 분들을 위해 오늘은 **생성자(Constructors)**에 대해 친근하게 설명해드릴게요. 생성자는 새로운 객체를 초기화하는 데 사용되는 특별한 기능이에요. 쉽게 말해, 새로운 객체를 만들 때 필요한 정보를 넘겨주는 문이라고 생각하면 돼요.

## 기본 생성자 이해하기

### 기본 개념
생성자는 클래스를 정의할 때 객체를 처음 만들 때 필요한 초기 설정을 하는 역할을 해요. 코틀린에서는 별도의 `new` 키워드 없이도 생성자를 호출할 수 있어요. 예를 들어, 다음과 같은 간단한 `Wombat` 클래스를 살펴봅시다:

```kotlin
// 생성자 예제: Wombat 클래스
class Wombat

fun main() {
    val wombat = Wombat()  // 생성자를 호출하여 Wombat 객체 생성
    println(wombat)       // 출력: wombat (기본 생성자인 경우 추가 정보 없이 생성됨)
}
```

여기서 `Wombat()` 호출이 객체를 생성하는 역할을 해요. 만약 다른 객체 지향 언어에서 왔다면 `new Wombat()`와 비슷하게 느껴질 수 있지만, 코틀린에서는 `new`를 생략해도 돼요.

### 매개변수를 이용한 생성자
생성자는 객체를 초기화할 때 필요한 정보를 매개변수로 받을 수 있어요. 예를 들어, `Alien` 클래스에서는 이름을 매개변수로 받아 초기화해요:

```kotlin
// 생성자 예제: Alien 클래스
class Alien(val name: String) {
    val greeting = "Poor $name!"
}

fun main() {
    val alien = Alien("Mr. Meeseeks")
    println(alien.greeting)  // 출력: Poor Mr. Meeseeks!
    // alien.name  // 오류: constructor parameter 'name' is inaccessible
}
```

위 코드에서 `name` 매개변수는 객체 내부에서만 사용되고 외부에서 직접 접근할 수 없어요. 만약 외부에서도 접근하고 싶다면 `var` 또는 `val`로 선언해야 해요:

```kotlin
// 생성자 예제: 이름이 외부에서도 접근 가능한 Alien 클래스
class MutableNameAlien(var name: String)  // var로 외부에서 변경 가능
class FixedNameAlien(val name: String)   // val로 읽기 전용

fun main() {
    val alien1 = MutableNameAlien("Reverse Giraffe")
    alien1.name = "Parasite"  // 변경 가능

    val alien2 = FixedNameAlien("Krombopolis Michael")
    // alien2.name = "Parasite"  // 오류: 읽기 전용이므로 변경 불가
}
```

### 여러 매개변수를 가진 생성자
클래스는 여러 매개변수를 가진 생성자도 가질 수 있어요. 예를 들어, `AlienSpecies` 클래스는 여러 속성을 초기화하는 데 사용될 수 있어요:

```kotlin
// 생성자 예제: 여러 매개변수를 가진 AlienSpecies 클래스
class AlienSpecies(
    val name: String,
    val eyes: Int,
    val hands: Int,
    val legs: Int
) {
    fun describe(): String {
        return "$name with $eyes eyes, $hands hands and $legs legs"
    }
}

fun main() {
    val kevin = AlienSpecies("Zigerion", 2, 2, 2)
    val mortyJr = AlienSpecies("Gazorpian", 2, 6, 2)

    println(kevin.describe())  // 출력: Zigerion with 2 eyes, 2 hands and 2 legs
    println(mortyJr.describe())  // 출력: Gazorpian with 2 eyes, 6 hands and 2 legs
}
```

## toString() 메서드 이해하기
객체를 문자열로 출력할 때 기본적으로 `toString()` 메서드가 호출되요. 기본 `toString()`은 객체의 메모리 주소를 보여주기 때문에 사용하기 불편할 수 있어요. 그래서 필요에 따라 `toString()`을 재정의할 수 있어요:

```kotlin
// toString() 예제: Scientist 클래스
class Scientist(val name: String) {
    override fun toString(): String {
        return "Scientist('$name')"
    }
}

fun main() {
    val zeep = Scientist("Zeep Xanflorp")
    println(zeep)  // 출력: Scientist('Zeep Xanflorp')
}
```

여기서 `override` 키워드는 기존의 `toString()` 메서드를 재정의한다는 것을 알려줘요. 이렇게 하면 객체의 내용을 더 쉽게 이해할 수 있어요.

## 핵심 요약
1. **생성자**는 객체를 초기화하는 데 사용되며, 클래스 정의와 함께 호출됩니다.
2. **매개변수**를 사용하면 객체 생성 시 필요한 정보를 전달할 수 있어요.
3. **외부 접근**을 원할 경우 매개변수를 `var` 또는 `val`로 선언해야 해요.
4. **여러 매개변수**로 복잡한 객체도 초기화할 수 있어요.
5. **toString()** 메서드를 재정의하면 객체를 더 유용하게 출력할 수 있어요.

이렇게 생성자를 이해하고 활용하면 코틀린 프로그래밍에서 객체를 효과적으로 다룰 수 있을 거예요! 질문이 있으면 언제든지 물어보세요! 😊