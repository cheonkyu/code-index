# 10. Booleans

안녕하세요! 이번 챕터에서는 코틀린 프로그래밍에서 Boolean 값을 다루는 방법에 대해 배워볼게요. Boolean은 `참(true)` 또는 `거짓(false)` 두 가지 상태를 표현하는 데이터 타입이에요. 이 내용을 이해하면 더 복잡한 조건문과 반복문을 작성하는 데 큰 도움이 될 거예요. 그럼 하나씩 차근차근 살펴볼게요!

## Boolean 연산자 소개

### `!` 연산자 - 부정 연산자
- `!` 연산자는 Boolean 값을 반전시켜 줘요. 예를 들어, `true`는 `false`로, `false`는 `true`로 바뀌어요.

### `&&` 연산자 - 논리곱 (AND)
- `&&` 연산자는 왼쪽과 오른쪽 모두 `true`일 때만 `true`를 반환해요.
  ```kotlin
  fun exampleAnd() {
      val isSunny = true
      val isWindy = false
      val result = isSunny && isWindy  // false
      println("결과: $result")  // 결과: false
  }
  ```

### `||` 연산자 - 논리합 (OR)
- `||` 연산자는 왼쪽이나 오른쪽 중 하나라도 `true`면 `true`를 반환해요.
  ```kotlin
  fun exampleOr() {
      val isSunny = true
      val isRainy = false
      val result = isSunny || !isRainy  // true
      println("결과: $result")  // 결과: true
  }
  ```

## 예제: 비즈니스 오픈/클로즈 확인

코틀린에서 비즈니스가 열려 있는지 닫혀 있는지 확인하는 예제를 살펴볼게요.

### 비즈니스가 열려 있는지 확인하기
```kotlin
fun isOpen(hour: Int) {
    val openHour = 9
    val closeHour = 20
    println("영업 시간: $openHour - $closeHour")
    val status = if (hour >= openHour && hour <= closeHour) {  // 1번 줄
        true
    } else {
        false
    }
    println("영업 중: $status")  // 영업 중이 아님: false
}

fun main() {
    isOpen(6)  // 출력: 영업 시간: 9 - 20, 영업 중이 아님: false
}
```
**핵심 요약:**
- `&&` 연산자는 두 조건이 모두 참일 때 참을 반환해요.
- `if` 표현식을 사용하여 간단하게 조건을 체크할 수 있어요.

### 더 간결한 표현
만약 위 코드를 더 간결하게 작성하고 싶다면:
```kotlin
fun isOpenSimplified(hour: Int) {
    val openHour = 9
    val closeHour = 20
    println("영업 시간: $openHour - $closeHour")
    val status = hour >= openHour && hour <= closeHour  // 더 간결하게 작성
    println("영업 중: $status")
}

fun main() {
    isOpenSimplified(6)  // 출력: 영업 시간: 9 - 20, 영업 중이 아님: false
}
```
**핵심 요약:**
- 불필요한 `if-else` 구조 없이 조건을 직접 대입할 수 있어요.

### 비즈니스가 닫혀 있는지 확인하기
`||` 연산자를 사용하여 비즈니스가 닫혀 있는지 확인해 볼게요.
```kotlin
fun isClosed(hour: Int) {
    val openHour = 9
    val closeHour = 20
    println("영업 시간: $openHour - $closeHour")
    val status = hour < openHour || hour > closeHour  // 닫힌 조건 체크
    println("닫혀 있음: $status")  // 닫혀 있음: true (시간이 6인 경우)
}

fun main() {
    isClosed(6)  // 출력: 영업 시간: 9 - 20, 닫혀 있음: true
}
```
**핵심 요약:**
- `||` 연산자는 적어도 하나의 조건이 참이면 전체 표현식이 참이에요.

## Boolean 표현식의 평가 순서 이해하기

Boolean 표현식의 평가 순서는 결과에 큰 영향을 미칠 수 있어요. 주의해야 할 점을 보여드리죠.

```kotlin
fun main() {
    val sunny = true
    val hoursSleep = 6
    val exercise = false
    val temp = 55

    // [1]
    val happy1 = sunny && temp > 50 || exercise && hoursSleep > 7
    println("happy1: $happy1")  // true

    // [2]
    val sameHappy1 = (sunny && temp > 50) || (exercise && hoursSleep > 7)
    println("sameHappy1: $sameHappy1")  // true

    // [3]
    val notSame = (sunny && temp > 50 || exercise) && hoursSleep > 7
    println("notSame: $notSame")  // false
}
```
**핵심 요약:**
- **평가 순서는 기본적으로 `&&` 연산이 먼저 처리되고 그 다음에 `||` 연산이 처리됩니다.**
- **괄호를 사용하면 원하는 순서대로 연산을 명시할 수 있어요.**

## 반복문: `while` 키워드 사용하기

코틀린에서 반복 작업을 처리할 때 `while` 키워드를 사용할 수 있어요.

```kotlin
fun condition(i: Int) = i < 100

fun main() {
    var i = 0
    while (condition(i)) {  // 조건이 참인 동안 반복
        print(".")
        i += 10  // i가 10 증가
    }
    // 출력: ........
}
```
**핵심 요약:**
- `while` 루프는 주어진 Boolean 표현식이 참인 동안 코드 블록을 반복해요.
- 각 반복마다 조건식이 다시 평가되어 루프를 계속할지 멈출지 결정해요.

이렇게 Boolean 연산자와 반복문을 활용하면 코틀린 프로그래밍에서 복잡한 조건과 반복 작업을 효과적으로 처리할 수 있어요. 연습을 통해 더 익숙해지세요! 궁금한 점이 있으면 언제든지 물어보세요!