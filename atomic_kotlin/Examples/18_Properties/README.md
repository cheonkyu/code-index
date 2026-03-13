# 18. Properties

안녕하세요! 코틀린 프로그래밍을 처음 배우는 여러분, 이번 챕터에서는 **속성(Properties)**에 대해 배워볼게요. 속성이란 클래스 내에서 상태를 유지하기 위해 사용하는 `var` 또는 `val` 변수를 말해요. 클래스를 사용하는 주된 이유 중 하나가 바로 이러한 상태를 유지하기 위함이에요. 그렇다면 `var` 속성과 `val` 속성의 차이점과 어떻게 사용하는지 자세히 알아볼게요!

## `var` 속성 vs `val` 속성

### `var` 속성
- **재할당 가능**: `var` 속성은 클래스의 인스턴스가 실행 중에 값을 변경할 수 있어요.
- **사용 예**: 
  ```kotlin
  class Cup {
      var percentFull = 0  // 컵의 채움 정도를 나타내는 변수
  }

  fun main() {
      val c1 = Cup()       // 컵 객체 생성
      c1.percentFull = 50  // 채움 정도를 50%로 설정
      val c2 = Cup()       // 다른 컵 객체 생성
      c2.percentFull = 100 // 채움 정도를 100%로 설정
      println(c1.percentFull)  // 출력: 50
      println(c2.percentFull)  // 출력: 100
  }
  ```

### `val` 속성
- **불변**: `val` 속성은 초기화 후에는 값을 변경할 수 없어요. 클래스의 상태를 불변으로 유지하는 데 유용해요.
- **사용 예**:
  ```kotlin
  class Cup2 {
      var percentFull = 0
      val max = 100       // 최대 채움 정도

      fun add(increase: Int): Int {
          percentFull += increase  // 채움 정도 증가
          if (percentFull > max)  // 최대값 초과 방지
              percentFull = max
          return percentFull
      }
  }

  fun main() {
      val cup = Cup2()  // 컵 객체 생성
      cup.add(50)       // 채움 정도 50 증가
      println(cup.percentFull)  // 출력: 50
      cup.add(70)       // 추가로 70 증가, 하지만 최대값으로 제한
      println(cup.percentFull)  // 출력: 100
  }
  ```

## 클래스 내부에서 속성 참조하기
클래스 내부의 멤버 함수는 객체 자신의 속성에 직접 접근할 수 있어요. 이때 `.` 표기법을 사용하긴 하지만, 함수 내에서는 명시적으로 `.`을 쓰지 않아도 돼요:
```kotlin
class Cup2 {
    var percentFull = 0
    val max = 100

    fun add(increase: Int): Int {
        percentFull += increase  // 직접 참조 가능
        if (percentFull > max)
            percentFull = max
        return percentFull
    }
}
```

## 전역 속성 (Top-Level Properties)
클래스 외부에서도 속성을 정의할 수 있어요. 하지만 주의할 점이 있어요:
- **`val`**: 불변 속성은 안전해요.
  ```kotlin
  val constant = 42  // 전역 불변 상수
  ```
- **`var`**: 가변 속성은 권장되지 않아요 (Anti-pattern). 여러 부분에서 수정될 수 있어 버그 발생 가능성이 높아요:
  ```kotlin
  var counter = 0  // 전역 가변 변수 (주의!)
  fun inc() {
      counter++
  }
  ```

## 불변 속성과 가변 속성의 혼동 이해하기
`val`은 재할당 불가능하지만, 객체 내의 가변 속성을 가질 수 있어요. 반대로 `var` 객체는 불변 속성을 가질 수 있어요. 예를 들어:

```kotlin
class House {
    var sofa: String = ""  // 집 객체의 소파는 가변
}

fun main() {
    val house = House()  // 집 객체 생성
    house.sofa = "Simple sleeper sofa: $89.00"  // 소파 내용 변경 가능
    println(house.sofa)  // 출력: Simple sleeper sofa: $89.00
    house.sofa = "New leather sofa: $3,099.00"  // 추가로 변경 가능
    println(house.sofa)  // 출력: New leather sofa: $3,099.00
    // 집 객체 자체를 `val`로 선언하면 안 됩니다: // house = House()  // 오류
}
```

```kotlin
class Sofa {
    val cover: String = "Loveseat cover"  // 소파 커버는 불변
}

fun main() {
    var sofa = Sofa()  // 소파 객체 생성 (가변)
    // sofa.cover = "New cover"  // 오류: 커버는 불변이기 때문에 직접 변경 불가
    sofa = Sofa()  // 하지만 새로운 객체로 재할당 가능
}
```

### 핵심 요약
- **`var`**: 재할당 가능, 상태 변경 가능
- **`val`**: 불변, 한 번 설정되면 변경 불가
- **클래스 내부 참조**: 멤버 함수는 `.` 없이 속성에 접근 가능
- **전역 속성 주의**: `var`는 복잡성 증가 가능성으로 조심해야 함
- **불변과 가변의 차이**: 객체 자체는 불변일 수 있지만 내부 속성은 가변일 수 있음

이해하셨나요? 궁금한 점이 있으면 언제든지 물어보세요! 함께 배우는 즐거움이 있기를 바래요! 😊