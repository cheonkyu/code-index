# 73. Exception Handling: 에러 처리의 기초

에러 처리는 프로그램이 예상치 못한 상황에서 안정적으로 작동할 수 있도록 도와주는 중요한 기능입니다. Kotlin에서는 컴파일 타임에 잡아내지 못하는 에러들을 런타임에 처리할 수 있도록 예외 처리 메커니즘을 제공합니다. 이번 챕터에서는 예외를 어떻게 정의하고, 잡아내며, 이를 통해 프로그램의 안정성을 높이는 방법에 대해 배워볼게요.

## 1. 예외 정의하기

### 기본 개념
- **예외(Exception)**: 프로그램 실행 중 발생하는 예기치 않은 상황을 나타냅니다.
- **Throwable**: 예외의 상위 클래스입니다. Kotlin에서는 `Throwable`을 상속받아 사용자 정의 예외를 만들 수 있습니다.

### 예제 코드: 사용자 정의 예외 정의하기

```kotlin
// ExceptionHandling/DefiningExceptions.kt
package exceptionhandling
import atomictest.*

// 기본 예외 클래스 상속
class Exception1(val value: Int) : Exception("wrong value: ${value}")

// 다시 상속하여 새로운 특성 추가
open class Exception2(description: String) : Exception(description)

// 상위 클래스 상속 받아 세부 조정
class Exception3(description: String) : Exception2(description)

fun main() {
    // 예외 던지기
    capture {
        throw Exception1(13)
    } eq "Exception1: wrong value: 13"
    
    capture {
        throw Exception3("error")
    } eq "Exception3: error"
}
```

**설명**:
- `Exception1`은 특정 값에 대한 오류 메시지를 포함하는 예외입니다.
- `Exception2`는 더 일반적인 예외 메시지를 허용합니다.
- `Exception3`은 `Exception2`를 상속받아 더욱 구체화된 예외 메시지를 제공합니다.

## 2. 예외 처리하기 (Catching Exceptions)

### 기본 개념
- **Catch 블록**: 예외를 잡아내는 코드 블록입니다. `try-catch` 구조를 사용합니다.
- **Recovery**: 예외가 발생했을 때 프로그램을 안정 상태로 되돌리는 과정입니다. 이는 오류 메시지 출력, 로그 기록 등이 포함될 수 있습니다.

### 예제 코드: 예외 처리와 스택 트레이스 살펴보기

```kotlin
// ExceptionHandling/Stacktrace.kt
package stacktrace
import exceptionhandling.Exception1

fun function1(): Int = throw Exception1(-52)
fun function2() = function1()
fun function3() = function2()
fun main() {
    // 함수 호출
    // function3()  // 주석 해제하면 스택 트레이스 출력
}
```

**설명**:
- `function1`에서 예외를 발생시키고, 이 예외는 호출 스택을 따라 위로 전파됩니다.
- 주석 해제하면 예외가 `main` 함수까지 도달하고 스택 트레이스가 출력됩니다:
  ```
  Exception in thread "main" exceptionhandling.Exception1: wrong value: -52
  at stacktrace.StacktraceKt.function1(Stacktrace.kt:6)
  at stacktrace.StacktraceKt.function2(Stacktrace.kt:8)
  at stacktrace.StacktraceKt.function3(Stacktrace.kt:10)
  at stacktrace.StacktraceKt.main(Stacktrace.kt:13)
  at stacktrace.StacktraceKt.main(Stacktrace.kt)
  ```

### 예외 처리 예제 코드

```kotlin
// ExceptionHandling/Handlers.kt
package exceptionhandling
import atomictest.eq

fun toss(x: Int): String {
    return when (x) {
        1 -> "Exception 1 occurred"
        2 -> "Exception 2 occurred"
        3 -> "Exception 3 occurred"
        else -> "OK"
    }
}

fun test() {
    try {
        println(toss(1))  // 예외 발생
    } catch (e: Exception1) {
        println("Caught Exception1: ${e.message}")
    } catch (e: Exception2) {
        println("Caught Exception2: ${e.message}")
    } catch (e: Exception3) {
        println("Caught Exception3: ${e.message}")
    } finally {
        println("작업 완료 후 정리 작업")
    }
}

fun main() {
    test()
}
```

**설명**:
- `toss` 함수는 입력에 따라 다양한 예외를 발생시킵니다.
- `test` 함수에서는 `try-catch` 구조를 사용해 각 예외를 처리합니다.
- `finally` 블록은 예외 발생 여부와 상관없이 항상 실행되는 코드 블록으로, 리소스 정리 등에 사용됩니다.

## 주요 핵심 개념 요약

1. **예외 정의**: `Throwable`을 상속받아 사용자 정의 예외를 만듭니다.
2. **예외 처리**: `try-catch` 구조를 사용해 예외를 잡아내고, 필요한 복구 작업을 수행합니다.
3. **스택 트레이스**: 예외 발생 시 호출 스택의 경로를 보여주며 문제 해결에 도움을 줍니다.
4. **자원 정리**: `finally` 블록을 통해 예외 발생 후에도 필요한 리소스 정리 작업을 보장합니다.

이렇게 예외 처리를 적절히 활용하면 프로그램의 안정성과 신뢰성이 크게 향상됩니다. 초보자도 이러한 기초적인 개념을 익혀두면 큰 도움이 될 거예요! 질문 있으시면 언제든지 물어보세요! 😊