# 07. IfExpressions: 조건문 이해하기

안녕하세요! 코틀린 프로그래밍을 처음 접하는 분들을 위해 이번 챕터에서는 `if` 표현식에 대해 친근하게 설명해드릴게요. 조건문은 프로그램이 특정 상황에 따라 다른 동작을 수행할 수 있게 해주는 중요한 도구랍니다. 그럼 지금부터 차근차근 배워볼게요!

## 조건이 맞으면 실행되는 `if` 문

`if` 문은 주어진 조건이 참(True)인지 거짓(False)인지 확인하고, 그 결과에 따라 특정 코드 블록을 실행하는 기능을 해요. 조건은 주로 불리언(Boolean) 값을 반환하는 표현식으로 이루어져 있어요. 예를 들어, 숫자 비교를 통해 불리언 값을 얻을 수 있어요.

### 기본 예제

```kotlin
fun main() {
    if (1 > 0)  // 1이 0보다 크므로 참(True)
        println("It's true!")  // 조건이 참이면 이 줄 실행

    if (10 < 11) {  // 10이 11보다 작으므로 참(True)
        println("10 < 11")
        println("ten is less than eleven")
    }
}
/* 출력 결과:
It's true!
10 < 11
ten is less than eleven
*/
```

**핵심 개념:**
- `if` 뒤의 괄호 안에는 불리언 값을 반환하는 표현식이 와야 해요.
- 참이면 해당 블록 안의 코드를 실행합니다. 여러 줄을 실행하려면 중괄호 `{}`를 사용하세요.

## 불리언 표현식 재사용

불리언 표현식을 여러 곳에서 재사용할 수 있어요. 이렇게 하면 코드를 더 간결하게 만들 수 있답니다.

### 불리언 변수 사용 예제

```kotlin
fun main() {
    val x: Boolean = 1 >= 1  // 불리언 변수 x에 값 할당
    if (x)  // x가 참이면
        println("It's true!")
}
/* 출력 결과:
It's true!
*/
```

**핵심 개념:**
- 불리언 변수를 생성하여 조건을 재사용할 수 있어요.
- `if (x)` 형태로 불리언 변수를 직접 조건으로 사용 가능합니다.

## `else` 키워드로 양쪽 경로 처리하기

`else` 키워드를 사용하면 참과 거짓 둘 다 처리할 수 있어요. 여러 조건을 순차적으로 검사할 수도 있답니다.

### 참/거짓 경로 처리 예제

```kotlin
fun main() {
    val n: Int = -11
    if (n > 0)  // n이 양수일 때
        println("It's positive")
    else  // 그렇지 않으면
        println("It's negative or zero")
}
/* 출력 결과:
It's negative or zero
*/

fun main() {
    val n: Int = -11
    if (n > 0)  // 첫 번째 조건
        println("It's positive")
    else if (n == 0)  // 두 번째 조건
        println("It's zero")
    else  // 마지막 조건
        println("It's negative")
}
/* 출력 결과:
It's negative
*/
```

**핵심 개념:**
- `else if`를 사용하여 여러 조건을 순차적으로 검사할 수 있어요.
- `else`는 `if`와 함께 사용되어야 합니다.

## 비교 연산자 이해하기

- `>=` : 왼쪽 값이 오른쪽 값보다 크거나 같을 때 참
- `<=` : 왼쪽 값이 오른쪽 값보다 작거나 같을 때 참
- `==` : 두 값이 같을 때 참 (문자열 비교 등에도 사용)
- `!=` : 두 값이 다를 때 참 (부등호 비교)

### 예시 코드

```kotlin
fun main() {
    val y: Boolean = false
    if (!y)  // !y는 y가 거짓일 때 참
        println("!y is true")  // 출력: !y is true
}
/* 출력 결과:
!y is true
*/
```

**핵심 개념:**
- `!` 연산자는 불리언 값의 반대를 반환해요.

## `if` 표현식을 이용한 결과 반환

`if` 표현식은 결과를 직접 반환할 수 있어요. 이렇게 하면 변수에 결과를 저장할 수 있어요.

### 결과 반환 예제

```kotlin
fun main() {
    val num = 10
    val result = if (num > 100)  // 조건 평가
        4  // 조건 참일 때의 결과
    else  // 조건 거짓일 때의 결과
        42
    println(result)  // 출력: 42 (조건이 거짓이므로 else의 값)
}
/* 출력 결과:
42
*/
```

**핵심 개념:**
- `if` 표현식 자체가 결과를 반환할 수 있어요.
- 조건이 참이면 첫 번째 값을, 거짓이면 두 번째 값을 결과로 반환합니다.

## 함수에서 `if` 사용하기

`if` 문을 함수 안에서도 사용할 수 있어요. 불리언 매개변수를 받아서 결과를 반환할 수 있답니다.

### 함수 예제

```kotlin
fun trueOrFalse(exp: Boolean): String {
    if (exp)  // 매개변수 exp가 참이면
        return "It's true!"  // 이 줄 실행
    else  // 그렇지 않으면
        return "It's false"  // 이 줄 실행
}

fun main() {
    val b = 1
    println(trueOrFalse(b < 3))  // 출력: It's true!
    println(trueOrFalse(b >= 3))  // 출력: It's false
}
/* 출력 결과:
It's true!
It's false
*/

// `else` 키워드를 사용한 간결한 버전
fun oneOrTheOther(exp: Boolean): String = if (exp) "True!" else "False"

fun main() {
    val x = 1
    println(oneOrTheOther(x == 1))  // 출력: True!
    // println(oneOrTheOther(x != 1))  // 예시 추가
}
```

**핵심 개념:**
- 함수 내에서 `if`를 사용하여 불리언 조건에 따라 다른 결과를 반환할 수 있어요.
- `else`를 사용하면 코드를 더 간결하게 작성할 수 있습니다.

이렇게 `if` 표현식을 이해하고 활용하면 코틀린 프로그래밍에서 조건에 따른 동작을 효과적으로 제어할 수 있어요. 연습을 통해 더 익숙해지세요! 질문 있으면 언제든지 물어보세요! 😊