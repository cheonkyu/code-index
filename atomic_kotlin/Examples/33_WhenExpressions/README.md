# 33. WhenExpressions: 간단하게 알아보는 코틀린의 `when` 표현식

안녕하세요! 코틀린 프로그래밍을 처음 접하시는 분들을 위해 `when` 표현식에 대해 쉽게 설명해 드릴게요. `when` 표현식은 특정 조건에 따라 다양한 동작을 간단하게 처리할 수 있게 해주는 강력한 도구랍니다. 특히 여러 선택지가 있을 때 `when` 표현식은 `if` 문보다 훨씬 직관적이고 간결해요.

## 기본 개념 이해하기

`when` 표현식은 다음과 같은 구조를 가지고 있어요:

```kotlin
when (비교할 값) {
    매치 표현식 1 -> 결과 표현식 1
    매치 표현식 2 -> 결과 표현식 2
    ...
    else -> 기본값 표현식 (선택사항)
}
```

- **when**: `when` 키워드로 표현식 시작.
- **비교할 값**: 실제 검사할 값이 들어갑니다.
- **매치 표현식**: 비교할 값이 특정 조건을 만족할 때 사용되는 표현식입니다. 화살표 `>`를 사용해서 매치와 결과를 구분해요.
- **결과 표현식**: 매치가 성공하면 해당 표현식이 실행되어 결과를 반환합니다.
- **else**: 모든 매치가 실패할 경우 실행되는 기본 동작을 정의합니다. 이 부분은 선택사항이지만, 코드의 완전성을 위해 종종 포함시킵니다.

### 예제: 독일의 순서수 표현하기

아래 예제는 정수를 받아 독일어로 순서수를 표현하는 함수 `ordinal`을 보여줍니다.

```kotlin
package whenexpressions

import atomictest.eq

// 숫자와 독일어 순서수 매핑
val numbers = mapOf(
    1 to "eins", 2 to "zwei", 3 to "drei",
    4 to "vier", 5 to "fuenf", 6 to "sechs",
    7 to "sieben", 8 to "acht", 9 to "neun",
    10 to "zehn", 11 to "elf", 12 to "zwoelf",
    13 to "dreizehn", 14 to "vierzehn",
    15 to "fuenfzehn", 16 to "sechzehn",
    17 to "siebzehn", 18 to "achtzehn",
    19 to "neunzehn", 20 to "zwanzig"
)

// 함수 정의: 정수를 받아 독일어 순서수를 반환
fun ordinal(i: Int): String {
    return when (i) {
        1 -> "erste"  // 1은 특별한 경우로 처리
        3 -> "dritte" // 3은 특별한 경우로 처리
        7 -> "siebte" // 7은 특별한 경우로 처리
        8 -> "achte"  // 8은 특별한 경우로 처리
        20 -> "zwanzigste" // 20은 특별한 경우로 처리
        else -> numbers[i] + "te" // 나머지 경우 숫자에 "te"를 붙임
    }
}

// 테스트 코드
fun main() {
    println(ordinal(2) eq "zweite") // 예상 결과: 오류 (2는 매치되지 않음)
    println(ordinal(3) eq "dritte") // 예상 결과: true
    println(ordinal(11) eq "elfte") // 예상 결과: true
}
```

**핵심 포인트:**
- `when` 표현식은 여러 조건을 쉽게 비교하고 각각에 대한 동작을 정의할 수 있어요.
- 매치가 성공하면 해당 매치 뒤에 오는 표현식이 실행됩니다.
- `else`는 필수는 아니지만, 모든 경우를 커버하여 코드의 완전성을 보장합니다.

### 예제: 좌표 처리하기

다음 예제는 사용자 입력에 따라 좌표를 조정하는 방법을 보여줍니다.

```kotlin
package whenexpressions

import atomictest.*

class Coordinates {
    var x: Int = 0
        set(value) {
            println("x gets $value") // 설정 시 동작 로그 출력
            field = value
        }
    var y: Int = 0
        set(value) {
            println("y gets $value") // 설정 시 동작 로그 출력
            field = value
        }

    override fun toString() = "($x, $y)" // 문자열 표현
}

// 입력 처리 함수
fun processInputs(inputs: List<String>) {
    val coordinates = Coordinates()
    for (input in inputs) {
        when (input) {
            "up", "u" -> coordinates.y-- // 위로 이동
            "down", "d" -> coordinates.y++  // 아래로 이동
            "left", "l" -> coordinates.x-- // 왼쪽으로 이동
            "right", "r" -> {
                println("Moving right") // 오른쪽 이동 로그 출력
                coordinates.x++
            }
            "nowhere" -> {} // 아무 동작도 하지 않음
            "exit" -> return // 함수 종료
            else -> println("bad input: $input") // 잘못된 입력 로그 출력
        }
    }
}

// 테스트 코드
fun main() {
    processInputs(listOf("up", "d", "nowhere", "left", "right", "exit", "r"))
    println("Output: ${coordinates}") // 결과 출력
}
```

**핵심 포인트:**
- 여러 입력에 따라 다양한 동작을 간결하게 처리할 수 있어요.
- `when` 표현식 내부에서 여러 동작을 블록으로 묶을 수 있어요.
- `else`는 잘못된 입력에 대한 처리를 용이하게 해줍니다.

이렇게 `when` 표현식을 사용하면 복잡한 조건 분기를 깔끔하게 관리할 수 있어요. 코드가 더 읽기 쉽고 유지보수하기도 편리해집니다. 연습을 통해 익숙해지시면 프로그래밍이 더욱 즐거워질 거예요! 질문 있으시면 언제든지 물어보세요. 😊