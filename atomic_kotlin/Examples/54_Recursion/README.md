# 54. Recursion (재귀)

재귀(Recursion)는 함수가 자기 자신을 호출하는 프로그래밍 기법이에요. 초보자분들을 위해 쉽게 설명해드릴게요!

## 재귀란 무엇인가요?

재귀는 간단하게 말해서 함수가 자신을 다시 호출하는 방식이에요. 예를 들어, 팩토리얼(factorial) 계산이 대표적인 재귀 예시죠. 팩토리얼은 1부터 주어진 숫자까지의 곱셈을 의미하는데, 다음과 같이 정의할 수 있어요:

- `factorial(1)`은 `1`입니다.
- `factorial(n)`은 `n * factorial(n - 1)`이에요.

### 팩토리얼 예제 코드 (Kotlin)

```kotlin
// Recursion/Factorial.kt
package recursion
import atomictest.eq

fun factorial(n: Long): Long {
    if (n <= 1) return 1  // 기저 사례: n이 1이면 결과는 1
    return n * factorial(n - 1)  // 재귀 호출
}

fun main() {
    factorial(5) eq 120  // 결과 확인
    factorial(17) eq 355687428096000  // 결과 확인
}
```

### 핵심 개념 요약
1. **기저 사례 (Base Case):** 재귀 호출이 끝나는 조건을 말해요. 여기서는 `n <= 1`일 때 `1`을 반환해요.
2. **재귀 호출 (Recursive Call):** 함수가 자기 자신을 호출하는 부분이에요. 여기서는 `factorial(n - 1)`을 호출해요.

## 호출 스택과 재귀의 한계

재귀 호출은 편리하지만, 각 호출마다 스택에 프레임을 추가하므로 **StackOverflowError**가 발생할 수 있어요. 예를 들어, 호출 스택을 보여주는 간단한 예제를 보세요:

### 호출 스택 예제 코드 (Kotlin)

```kotlin
// Recursion/CallStack.kt
package recursion

fun fail() {
    // throw IllegalStateException()  // 주석 해제하면 예외 발생
}

fun illegalState() {
    throw IllegalStateException()  // 예외 발생
}

fun main() {
    fail()  // 예외가 발생하지 않으면 정상 작동
    // throw IllegalStateException()  // 주석 해제하면 예외 발생
}
```

### 예외 발생 시 스택 트레이스 예시

```plaintext
Exception in thread "main" java.lang.IllegalStateException
    at recursion.CallStackKt.illegalState(CallStack.kt:5)
    at recursion.CallStackKt.fail(CallStack.kt:8)
    at recursion.CallStackKt.main(CallStack.kt:11)
```

### 무한 재귀 (Infinite Recursion)

무한 재귀는 재귀 호출이 종료되지 않아 **StackOverflowError**를 일으키는 경우예요. 예를 들어:

```kotlin
// Recursion/InfiniteRecursion.kt
package recursion

fun recurse(i: Int): Int = recurse(i + 1)  // 계속 재귀 호출

fun main() {
    // println(recurse(1))  // 주석 해제하면 예외 발생
}
```

### 재귀의 한계 극복: 반복문 사용

재귀 호출이 너무 깊어지면 스택 오버플로우가 발생할 수 있어요. 이럴 때는 반복문(Iteration)을 사용하는 것이 더 안전해요:

```kotlin
// Recursion/Iteration.kt
package iteration

import atomictest.eq

fun sum(n: Long): Long {
    var accumu = 0L
    for (i in 1..n) {
        accumu += i
    }
    return accumu
}

fun main() {
    sum(2) eq 3  // 결과 확인
    sum(1000) eq 500500  // 결과 확인
    // sum(100_000) eq 500050000  // 주석 해제하면 StackOverflowError 발생 가능
    (1..100_000L).sum() eq 5000050000  // 반복문을 사용한 결과 확인
}
```

### 주요 핵심 개념 요약
1. **재귀 호출의 원리:** 함수가 자기 자신을 호출하여 문제를 작은 부분으로 나눕니다.
2. **기저 사례:** 재귀 호출이 멈추는 조건이 필요합니다.
3. **스택 오버플로우:** 재귀 호출이 너무 깊어지면 스택 오버플로우 에러가 발생할 수 있어요.
4. **반복문 대안:** 큰 수에 대한 재귀 호출 대신 반복문을 사용하면 안전성을 높일 수 있어요.

이제 재귀에 대한 기본 개념을 조금 더 이해하셨기를 바라요! 궁금한 점이 있으면 언제든지 물어보세요!