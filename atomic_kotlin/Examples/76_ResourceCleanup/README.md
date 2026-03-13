# 76. ResourceCleanup: 자원 정리의 중요성

안녕하세요! 코틀린 프로그래밍을 처음 배우는 여러분께 친절하게 설명해드리겠습니다. 이번 챕터에서는 프로그램에서 발생할 수 있는 예외 상황에서도 안전하게 자원을 정리하는 방법에 대해 알아보겠습니다. 특히 `finally` 문이 어떻게 작동하는지 이해하는 것이 중요해요. 자, 함께 배워볼까요?

## 핵심 개념 요약

### 1. **자원 정리의 필요성**
   - 프로그램에서 사용하는 자원(예: 파일 핸들, 네트워크 연결 등)은 반드시 정리해야 합니다. 예외가 발생하더라도 자원을 제대로 정리하지 않으면 메모리 누수나 시스템 오류가 발생할 수 있어요.

### 2. **`finally` 문의 역할**
   - `finally` 문은 `try` 블록이 어떻게 종료되든 상관없이 항상 실행되는 코드 블록입니다. 예외가 발생하든 정상적으로 종료되든, 자원을 정리하는 코드를 이곳에 넣어두면 안전하게 작동해요.

### 3. **예외 처리와 `finally`**
   - `try` 블록에서 예외가 발생하더라도 `finally` 블록은 반드시 실행되므로, 자원을 안전하게 해제할 수 있어요.

## 예제 코드 설명

### 예제 1: 기본적인 `finally` 사용

```kotlin
package exceptionhandling

import atomictest.*

// 값을 검사하는 함수
fun checkValue(value: Int) {
    try {
        print("${value}")  // 예시로 trace 대신 print 사용
        if (value <= 0) {
            throw IllegalArgumentException("값은 양수여야 합니다: $value")
        }
    } finally {
        print("${value}에 대한 finally 절 실행: 자원 정리")  // 자원 정리 메시지 출력
    }
}

fun main() {
    listOf(10, -10).forEach { value ->
        try {
            checkValue(it)
        } catch (e: IllegalArgumentException) {
            print("catch 절에서 예외 처리: ${e.message}")
        }
    }
}
```

**설명:**
- `checkValue` 함수에서 `try` 블록은 값을 검사하고 예외를 발생시킵니다.
- `finally` 블록은 예외가 발생하든 정상 종료되든 항상 실행되어 자원 정리 메시지를 출력합니다.
- `main` 함수에서는 예외가 발생하면 `catch` 블록에서 처리하고, 정상적으로 실행되면 `finally` 블록에서 자원 정리를 수행합니다.

### 예제 2: 중간 `catch` 문과 `finally`

```kotlin
package exceptionhandling

import atomictest.eq

data class Switch(
    var on: Boolean = false,
    var result: String = "OK"
)

// 스위치 조작 함수
fun testFinally(i: Int): Switch {
    val sw = Switch()
    try {
        sw.on = true
        when (i) {
            0 -> throw IllegalStateException("예외 발생")  // 예외 발생 조건
            1 -> return sw  // 예외 발생 시 반환
        }
    } catch (e: IllegalStateException) {
        sw.result = "예외"
    } finally {
        sw.on = false  // 자원 정리: 스위치 끄기
    }
    return sw
}

fun main() {
    println(testFinally(0) eq "Switch(on=false, result=예외)")  // 예외 처리
    println(testFinally(1) eq "Switch(on=false, result=OK)")  // 정상 처리
    println(testFinally(2) eq "Switch(on=false, result=OK)")  // 추가 조건 처리
}
```

**설명:**
- `testFinally` 함수에서 스위치를 켜고 예외를 발생시키거나 반환합니다.
- 예외가 발생하든 정상 종료되든 `finally` 블록에서 스위치를 끄는 자원 정리 작업을 수행합니다.
- `main` 함수에서는 다양한 입력에 대해 결과를 출력하여 `finally`의 동작을 확인합니다.

### 예제 3: `capture()` 함수를 이용한 예외 캡처

```kotlin
package exceptionhandling

import atomictest.CapturedException
import atomictest.eq

// 예외를 캡처하는 함수
fun capture(f: () -> Unit): CapturedException {
    try {
        f()  // 함수 호출
    } catch (e: Throwable) {
        return CapturedException(e::class, e.message ?: "")
    }
    return CapturedException(null, "<Error>: 예상된 예외가 발생하지 않았습니다")
}

fun main() {
    println(capture { throw Exception("!!!")} eq "Exception: !!!")  // 예외 발생
    println(capture { 1 } eq "<Error>: 예상된 예외가 발생하지 않았습니다")  // 예외 없음
}
```

**설명:**
- `capture` 함수는 주어진 함수 `f`를 실행하면서 예외를 캡처합니다.
- 예외가 발생하면 예외 클래스와 메시지를 포함한 `CapturedException` 객체를 반환합니다.
- 예외가 발생하지 않으면 예외가 예상되었다는 메시지를 반환합니다.

## 간단한 가이드라인

1. **논리 오류 처리:**
   - 가능한 한 예외를 잡지 않고 스택 트레이스를 통해 오류를 확인하세요.
   - 중요한 부분에서는 상위 레벨에서 예외를 잡아 애플리케이션 전체에 영향을 주지 않도록 처리하세요.

2. **데이터 오류 처리:**
   - 사용자 입력이나 외부 데이터에서 발생하는 예외는 적절히 처리해야 합니다.
   - 예를 들어, `String.toIntOrNull()`을 사용하면 예외 없이 안전하게 변환할 수 있어요.

**주의:** 예외 처리를 과도하게 사용하면 코드의 가독성을 떨어뜨릴 수 있으니, 예외가 발생한 이유를 찾고 수정하는 것이 주된 목적이 되도록 하세요!

이제 `finally` 문과 예외 처리에 대해 좀 더 잘 이해하셨기를 바라요! 질문이 있으면 언제든지 물어보세요! 😊