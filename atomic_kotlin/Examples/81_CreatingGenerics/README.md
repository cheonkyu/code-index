# 81. CreatingGenerics: 일반화된 코드 작성하기

안녕하세요! 코틀린 프로그래밍 초보자 여러분, 오늘은 **일반화된 코드**에 대해 배워볼게요. 쉽게 말해, 다양한 종류의 데이터를 처리할 수 있도록 코드를 더 유연하게 만드는 방법이죠. 이 주제는 코드의 범위를 넓히고 중복을 줄여 더 효율적인 프로그래밍을 가능하게 해줍니다.

## 일반화 코드란?

- **특정 타입 대신 나중에 지정되는 타입으로 작업하기**: 일반화된 코드는 아직 구체적인 타입이 정해지지 않은 상태에서 작동할 수 있어요. 예를 들어, 일반적인 클래스나 함수는 특정 타입만 다룰 수 있지만, 일반화된 코드는 나중에 정의될 수 있는 여러 타입과 함께 작동할 수 있어요.
- **고정된 타입의 제약 해소**: 특정 클래스만을 다루는 코드는 새로운 클래스가 추가될 때마다 수정이 필요해요. 하지만 일반화를 사용하면 같은 함수나 클래스를 다양한 타입에 적용할 수 있어 더 유연해집니다.

### Polymorphism (다형성)의 역할

다형성은 객체 지향 프로그래밍에서 타입을 넘어서 동작하는 능력을 제공해요. 예를 들어, 기본 클래스 객체를 매개변수로 받는 함수를 작성하면, 그 함수를 기본 클래스에서 파생된 모든 클래스의 객체와 함께 호출할 수 있어요. 이로 인해 코드의 재사용성이 향상되고 더 넓은 범위에서 활용 가능해집니다.

## 인터페이스와 일반화의 조합

- **인터페이스 사용**: 특정 클래스 대신 인터페이스를 사용하면 클래스 계층을 넘어서 작동할 수 있어요. 인터페이스를 구현하는 클래스는 인터페이스를 통해 공통 기능을 공유할 수 있어요. 예를 들어, 여러 클래스가 공통 인터페이스를 구현하면 그 인터페이스를 기반으로 작성된 함수를 다양한 클래스에 적용할 수 있어요.
  
  ```kotlin
  package creatinggenerics

  import atomictest.eq // 예시 패키지, 실제 사용 시 적절한 패키지 사용 필요

  // 인터페이스 정의
  interface Communicator {
      fun communicate(): String
  }

  // 인터페이스를 구현하는 클래스들
  class Person : Communicator {
      override fun communicate() = "Hi!"
  }

  class Dog : Communicator {
      override fun communicate() = "Ruff!"
  }

  class Robot : Communicator {
      override fun communicate() = "Beep!"
  }

  // 일반화된 함수 예시
  fun <T : Communicator> speak(communicator: T) = communicator.communicate()

  fun main() {
      val person = Person()
      val dog = Dog()
      val robot = Robot()

      println(speak(person)) // 출력: "Hi!"
      println(speak(dog))   // 출력: "Ruff!"
      println(speak(robot)) // 출력: "Beep!"
  }
  ```

### `Any` 타입의 한계와 활용

- **Any 타입**: 모든 Kotlin 클래스의 상위 타입으로, 모든 객체를 다룰 수 있어요. 하지만 `Any`는 매우 제한적이어서 주로 세 가지 메소드(`equals()`, `hashCode()`, `toString()`)만 제공해요.
  
  ```kotlin
  // Any 타입 사용 예시
  fun talk(speaker: Any) {
      when (speaker) {
          is Person -> println("${speaker.hashCode()}: Hi!")
          is Dog -> println("${speaker.hashCode()}: Ruff!")
          is Robot -> println("${speaker.hashCode()}: Beep!")
          else -> println("Not a talker")
      }
  }

  fun main() {
      val person = Person()
      val dog = Dog()
      val robot = Robot()

      talk(person) // 출력: "hashCode(): Hi!"
      talk(dog)   // 출력: "hashCode(): Ruff!"
      talk(robot) // 출력: "hashCode(): Beep!"
      talk(11)    // 출력: "Not a talker"
  }
  ```

  **주의**: `Any`를 사용하면 타입 안전성을 잃을 수 있어요. 따라서 타입이 명확한 경우에는 직접 타입 캐스팅을 통해 더 안전한 코드를 작성하는 것이 좋습니다.

## 일반화 타입과 함수 정의하기

- **일반화 타입 정의**: 일반화 타입은 `<>` 기호를 사용해 정의해요. 예를 들어, `T`라는 제네릭 타입 파라미터를 사용하면 다음과 같이 작성할 수 있어요.

  ```kotlin
  // 일반화 함수 예시
  fun <T> printDetails(data: T) {
      println("Type: ${data::class.qualifiedName}")
      println("Details: ${data}")
  }

  fun main() {
      printDetails("안녕하세요") // 문자열 타입으로 실행
      printDetails(42)         // 정수 타입으로 실행
  }
  ```

### 핵심 요약

1. **일반화 코드**는 다양한 타입을 유연하게 처리할 수 있게 해줍니다.
2. **다형성**을 활용하면 기본 클래스를 기반으로 여러 하위 클래스와 함께 작동하는 함수를 작성할 수 있어요.
3. **인터페이스**는 클래스 계층을 넘어서 동작할 수 있게 해줍니다.
4. **`Any` 타입**은 매우 유연하지만 타입 안전성을 잃을 수 있으므로 주의가 필요해요.
5. **일반화 타입**을 사용하면 코드 중복을 줄이고 다양한 타입에 대해 재사용 가능한 함수를 작성할 수 있어요.

이제 여러분도 코틀린에서 일반화된 코드를 작성해보면서 더 유연하고 효율적인 프로그래밍을 경험해보세요! 질문이 있으면 언제든지 물어보세요!