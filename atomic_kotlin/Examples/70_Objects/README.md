# 70. Objects

안녕하세요! 코틀린 프로그래밍 초보자 여러분, 오늘은 **Objects**에 대해 배워볼게요. Objects는 코틀린에서 클래스와 비슷해 보이지만, 특별한 역할을 하는 개념이에요. 핵심 내용을 쉽게 이해할 수 있도록 하나씩 살펴보도록 하죠!

## 단일 인스턴스 객체 (Singleton Pattern)

### 기본 개념
- **Object 키워드**: `object`라는 키워드로 정의되며, 이는 하나의 단일 인스턴스만 생성되는 구조를 만듭니다. 이를 **Singleton 패턴**이라고 부르기도 해요.
- **사용 예시**:
  ```kotlin
  package objects
  import atomictest.eq

  object JustOne {
      val n = 2
      fun f() = n * 10
      fun g() = this.n * 20  // `this`는 객체 자신을 가리킵니다.
  }

  fun main() {
      JustOne.n eq 2          // 2
      JustOne.f() eq 20       // 2 * 10 = 20
      JustOne.g() eq 40       // 2 * 20 = 40
  }
  ```
- **주의사항**: 객체를 생성할 때 `JustOne()`처럼 인스턴스를 생성할 수 없어요. 객체는 정의되는 순간 이미 하나의 인스턴스가 생성되어 있으니까요.

### 명명 규칙
- **객체 명명**: 객체는 클래스처럼 대문자로 시작하는 명명 규칙을 따르는 것이 좋습니다. 예를 들어, `JustOne` 대신 `JustOneObject`를 사용할 수도 있지만, 일반적으로는 단순히 대문자로 시작하는 이름을 선호합니다.

## 객체의 상속과 인터페이스

### 상속 예시
- **클래스 상속**: 객체도 일반 클래스처럼 상속을 받을 수 있어요.
  ```kotlin
  package objects
  import atomictest.eq

  open class Paint(val color: String) {
      open fun apply() = "Applying $color"
  }

  object Acrylic: Paint("Blue") {
      override fun apply() = "Acrylic, ${super.apply()}"
  }

  interface PaintPreparation {
      fun prepare(): String
  }

  object Prepare: PaintPreparation {
      override fun prepare() = "Scrape"
  }

  fun main() {
      Prepare.prepare() eq "Scrape"      // "Scrape"
      Paint("Green").apply() eq "Applying Green"  // "Applying Green"
      Acrylic.apply() eq "Acrylic, Applying Blue"  // "Acrylic, Applying Blue"
  }
  ```
- **인터페이스 상속**: 인터페이스를 구현하는 객체도 가능합니다.

## 전역 공유 객체 (Global Sharing Objects)

- **전역 접근**: 객체는 정의된 패키지 외부에서도 접근 가능하며, 같은 객체 인스턴스를 공유합니다.
  ```kotlin
  // objectsharing 패키지
  package objectsharing
  object Shared {
      var i: Int = 0
  }

  // 다른 패키지에서 접근
  // objectshare1 패키지
  package objectshare1
  import objectsharing.Shared

  fun f() {
      Shared.i += 5
  }

  // objectshare2 패키지
  package objectshare2
  import objectsharing.Shared
  import objectshare1.f
  import atomictest.eq

  fun g() {
      Shared.i += 7
  }

  fun main() {
      f()
      g()
      Shared.i eq 12  // 결과 확인
  }
  ```
- **프라이버시 설정**: 객체를 `private`로 설정하면 다른 패키지에서 접근이 불가능해집니다.

## 객체의 중첩

- **중첩 객체**: 객체는 다른 객체나 클래스 내부에 정의될 수 있어요. 하지만 중첩된 클래스는 자기 자신을 포함할 수 없어요.
  ```kotlin
  // objects 패키지
  package objects
  import atomictest.eq

  object Outer {
      object Nested {
          val a = "Outer.Nested.a"
      }
  }

  class HasObject {
      object Nested {
          val a = "HasObject.Nested.a"
      }
  }

  fun main() {
      Outer.Nested.a eq "Outer.Nested.a"  // "Outer.Nested.a"
      HasObject.Nested.a eq "HasObject.Nested.a"  // "HasObject.Nested.a"
  }
  ```
- **컴패니언 객체**: 클래스 내부에 객체를 정의하는 방법 중 하나로, `companion object`라고 불립니다. 이 부분은 나중에 더 자세히 다루도록 할게요!

## 요약
- **단일 인스턴스**: `object` 키워드로 하나의 유일한 인스턴스를 생성합니다.
- **상속과 인터페이스**: 객체도 클래스처럼 상속과 인터페이스 구현이 가능합니다.
- **공유**: 객체는 정의된 패키지 외부에서도 공유됩니다.
- **중첩**: 객체는 다른 객체나 클래스 내부에 정의될 수 있습니다.

이제 코틀린 객체에 대해 조금 더 친숙해졌나요? 연습 문제를 통해 직접 코드를 작성해보면 더 잘 이해할 수 있을 거예요. 자세한 예제와 해결 방법은 [AtomicKotlin 웹사이트](www.AtomicKotlin.com)를 참고해보세요! 궁금한 점이 있으면 언제든지 물어보세요!