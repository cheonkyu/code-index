# 52. 로컬 함수 (Local Functions)

안녕하세요! 코틀린 프로그래밍을 처음 접하는 분들을 위해 로컬 함수에 대해 쉽게 설명해드릴게요. 로컬 함수는 프로그래밍에서 코드 중복을 줄이고 코드를 더 깔끔하게 유지하는 데 큰 도움이 되는 기능입니다. 이제 초보자 분들도 이해하기 쉽게 핵심 개념과 예제들을 살펴보도록 하겠습니다.

## 핵심 개념

### 1. 정의와 사용 범위
- **로컬 함수**는 다른 함수 내부에서 정의되는 함수입니다. 정의된 범위 내에서만 사용 가능하고 외부로 노출되지 않아 코드의 가독성을 높이고 중복 코드를 줄일 수 있습니다.
- 예를 들어, `log()` 함수는 `main()` 함수 안에 정의되지만 외부에서 직접 호출할 수는 없습니다.

### 2. 클로저 특성
- 로컬 함수는 **클로저**로 작동합니다. 즉, 외부 스코프의 변수나 값을 캡처하여 직접 매개변수로 전달할 필요 없이 사용할 수 있습니다. 이는 코드를 간결하게 만듭니다.

### 3. 확장 함수와 익명 함수
- **확장 함수**는 특정 타입에 대한 추가 함수를 정의할 수 있습니다. 로컬 함수와 마찬가지로, 이들도 정의된 범위 내에서만 사용 가능합니다.
- **익명 함수**는 이름이 없는 함수로, `fun` 키워드를 사용하여 정의합니다. 로컬 함수와 유사하지만 이름이 없다는 차이가 있습니다.

## 예제 코드 설명

### 예제 1: 로컬 함수 사용하기
```kotlin
// LocalFunctions/LocalFunctions.kt
import atomictest.eq

fun main() {
    val logMsg = StringBuilder()

    // 로컬 함수 정의
    fun log(message: String) {
        logMsg.appendLine(message)
    }

    log("시작 계산")
    val x = 42 // 계산 모방
    log("계산 결과: $x")

    // 출력 확인
    logMsg.toString() eq """
        시작 계산
        계산 결과: 42
        """
}
```
- **설명**: `log()` 함수는 `main()` 함수 안에서 정의되어 `logMsg` 변수를 사용합니다. 외부에서 호출할 수 없지만 내부에서 중복 코드를 줄여줍니다.

### 예제 2: 확장 함수 만들기
```kotlin
// LocalFunctions/LocalExtensions.kt
import atomictest.eq

fun main() {
    // 확장 함수 정의
    fun String.exclaim(): String {
        return "$this!"
    }

    println("Hello".exclaim()) eq "Hello!"
    println("Hallo".exclaim()) eq "Hallo!"
    println("Bonjour".exclaim()) eq "Bonjour!"
    println("Ciao".exclaim()) eq "Ciao!"
}
```
- **설명**: `String` 타입에 `exclaim()` 확장 함수를 추가하여 문자열 뒤에 "!"를 붙이는 기능을 제공합니다. 이 함수는 `main()` 함수 내에서만 사용 가능합니다.

### 예제 3: 로컬 함수 참조하기
```kotlin
// LocalFunctions/LocalFunctionReference.kt
import localfunctions.*
import atomictest.eq

fun main() {
    fun interesting(session: Session): Boolean {
        if (session.title.contains("Kotlin") && session.speaker in favoriteSpeakers) {
            return true
        }
        // 추가 검사 로직...
        return false
    }

    // 로컬 함수 참조
    sessions.any(::interesting) eq true
}
```
- **설명**: `interesting()` 함수는 `Session` 객체를 기반으로 특정 조건을 확인합니다. 이 함수는 `main()` 함수 내에서만 사용 가능하며, `any()` 함수에 함수 참조로 전달됩니다.

### 예제 4: 익명 함수 사용하기
```kotlin
// LocalFunctions/InterestingSessions.kt
import localfunctions.*
import atomictest.eq

fun main() {
    sessions.any(
        fun(session: Session): Boolean {
            if (session.title.contains("Kotlin") && session.speaker in favoriteSpeakers) {
                return true
            }
            // 추가 검사 로직...
            return false
        }
    ) eq true
}
```
- **설명**: 이 예제에서는 익명 함수를 사용해 `sessions` 리스트에서 특정 조건을 만족하는 세션을 찾습니다. 익명 함수는 이름이 없지만 로컬 함수와 유사한 방식으로 동작합니다.

### 예제 5: 반환 표현식과 레이블된 반환
```kotlin
// LocalFunctions/ReturnFromFun.kt
import atomictest.eq

fun main() {
    val list = listOf(1, 2, 3, 4, 5)
    val value = 3
    var result = ""

    list.forEach {
        result += "$it"
        if (it == value) {
            result eq "123"  // [1] 이곳에서 반환하면 main() 함수 전체가 종료됩니다.
            return  // [2] 하지만 반환되지 않아 마지막 코드 실행
        }
    }
    result eq "Never gets here"  // [2] 출력되지 않음
}
```
- **설명**: `forEach` 내에서 반환 표현식은 호출 범위인 `main()` 함수 전체를 종료합니다. 레이블된 반환(`return@forEach`)을 사용하면 람다 내부에서만 반환할 수 있습니다.

---

이렇게 로컬 함수를 사용하면 코드가 더 깔끔해지고 중복을 줄일 수 있습니다. 초보자 분들도 로컬 함수의 개념을 이해하고 예제 코드를 통해 실습해보면서 점점 익숙해질 수 있을 거예요! 궁금한 점이 있으면 언제든지 물어보세요!