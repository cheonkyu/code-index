# 34. 열거형 (Enumerations)

안녕하세요! 이번 챕터에서는 Kotlin에서 열거형(Enum)에 대해 배워볼게요. 열거형은 프로그래밍에서 특정 값들의 집합을 쉽게 관리할 수 있게 해주는 멋진 도구예요. 간단하게 말해서, 여러 이름이나 상태를 하나로 묶어서 코드를 깔끔하게 유지할 수 있게 돕는 거죠.

## 기본 개념

### 무엇이 열거형인가요?

열거형은 이름들의 모음이라고 생각하면 돼요. 예를 들어, 게임에서 캐릭터의 난이도를 나타낼 때 `Easy`, `Medium`, `Hard` 같은 값을 열거형으로 만들 수 있어요. Kotlin에서는 이런 이름들을 `enum class`로 쉽게 다룰 수 있게 해주고 있어요.

#### 예제 코드: 기본 열거형 정의

```kotlin
package enumerations

import atomictest.eq // 테스트 라이브러리 임포트

// 열거형 클래스 정의
enum class Level {
    Overflow, High, Medium, Low, Empty
}

fun main() {
    // 열거형 이름과 문자열 비교
    Level.Medium eq "Medium" // 출력 결과: true
}
```

### 열거형 이름 접근 방법

열거형 이름을 직접 참조할 때는 앞에서와 같이 `Level.Medium`처럼 명시적으로 작성해야 해요. 하지만 모든 이름을 현재 스코프에 가져오려면 `import`를 사용할 수 있어요.

#### 예제 코드: 이름 자동 임포트

```kotlin
import atomictest.eq // 테스트 라이브러리 임포트
import enumerations.Level.* // Level 열거형의 모든 이름을 현재 스코프에 가져옴

fun main() {
    Overflow eq "Overflow" // 직접 명시하지 않아도 됩니다
    High eq "High"        // 마찬가지로 명시하지 않아도 됩니다
}
```

**핵심 요약:**
- `import enumerations.Level.*`를 통해 `Level` 열거형의 모든 값들을 현재 스코프에 가져올 수 있어요.
- 이렇게 하면 `Level.Medium` 대신 `Medium`만으로도 접근 가능해요.

### 열거형 값 반복 및 순서 활용

열거형의 모든 값을 반복하거나 순서를 확인할 수도 있어요.

#### 예제 코드: 열거형 값 반복 및 순서 활용

```kotlin
package enumerations

import atomictest.eq // 테스트 라이브러리 임포트

import enumerations.Size.* // Size 열거형의 모든 값을 현재 스코프에 가져옴

enum class Size {
    Tiny, Small, Medium, Large, Huge, Gigantic
}

fun main() {
    Gigantic eq "Gigantic" // 특정 값 확인
    Size.values().toList() eq listOf(Tiny, Small, Medium, Large, Huge, Gigantic) // 모든 값 확인
    Tiny.ordinal eq 0       // 첫 번째 값의 순서 확인
    Huge.ordinal eq 4       // 마지막 값의 순서 확인
}

// 핵심 요약:
- `values()`를 사용하면 모든 열거형 값을 반복할 수 있어요.
- 각 열거형 값은 `ordinal` 속성을 통해 순서를 확인할 수 있어요 (0부터 시작).

### 조건문을 활용한 다양한 동작

열거형 내 각 항목에 대해 특정 동작을 다르게 적용할 수도 있어요. `when` 표현식을 사용하면 쉽게 구현할 수 있어요.

#### 예제 코드: `when` 표현식 활용

```kotlin
package checkingoptions

import atomictest.*
import enumerations.Level
import enumerations.Level.*

fun checkLevel(level: Level) {
    when (level) {
        Overflow -> trace(">>> Overflow!") // 특정 동작
        Empty -> trace("Alert: Empty")    // 다른 동작
        else -> trace("Level $level OK") // 기본 동작
    }
}

fun main() {
    checkLevel(Empty)    // "Alert: Empty" 출력
    checkLevel(Low)      // "Level Low OK" 출력
    checkLevel(Overflow) // "Overflow!" 출력
    trace eq """
    Alert: Empty
    Level Low OK
    >>> Overflow!
    """ // 출력 확인
}

// 핵심 요약:
- `when` 표현식을 사용하면 열거형 값에 따라 다양한 동작을 쉽게 구현할 수 있어요.

### 열거형의 속성과 메서드

열거형은 속성과 메서드를 정의할 수 있어요. 이렇게 하면 각 값에 고유한 정보를 부여할 수 있어요.

#### 예제 코드: 속성과 메서드 정의

```kotlin
package enumerations

import atomictest.eq // 테스트 라이브러리 임포트
import enumerations.Direction.* // Direction 열거형의 모든 값을 현재 스코프에 가져옴

enum class Direction(val notation: String) {
    North("N"), South("S"),
    East("E"), West("W"); // 마지막 세미콜론 필수

    val opposite: Direction
        get() = when (this) {
            North -> South
            South -> North
            West -> East
            East -> West
        }
}

fun main() {
    North.notation eq "N" // 속성 접근
    North.opposite eq South // 메서드 사용 예시
    West.opposite.opposite eq West // 반대 방향 재귀 호출
    North.opposite.notation eq "S" // 반대 방향의 속성 접근
}

// 핵심 요약:
- 열거형 내에서 속성을 정의하면 각 항목에 대한 추가 정보를 쉽게 관리할 수 있어요.
- 메서드를 통해 각 항목에 대한 동적 동작을 구현할 수 있어요.

## 결론

열거형은 코드의 가독성을 높이고 특정 상태나 값들을 체계적으로 관리하는 데 정말 유용해요. 이를 통해 반복적인 코드를 줄이고 유지보수를 쉽게 만들 수 있어요. 연습을 통해 더 많은 기능을 활용해보세요!

**연습 자료:** [www.AtomicKotlin.com](http://www.AtomicKotlin.com)에서 추가 예제와 해답을 확인해보세요!

이제 여러분도 Kotlin 열거형을 좀 더 자신감 있게 다룰 수 있을 거예요. 열공하세요! 🚀