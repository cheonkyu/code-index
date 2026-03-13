# 43. Break와 Continue

안녕하세요! Kotlin 프로그래밍 초보자 여러분, 오늘은 `break`와 `continue`에 대해 배워볼게요. 이 두 기능은 반복문 안에서 특별한 제어를 할 수 있게 해주는 강력한 도구랍니다. 이해하기 쉽게 설명해드릴게요.

## 기본 개념

### What are `break`와 `continue`?

`break`와 `continue`는 반복문 안에서 실행 흐름을 조절하는 키워드예요. 

- **continue**: 현재 반복을 건너뛰고 다음 반복으로 바로 넘어가게 해줍니다.
- **break**: 반복문을 완전히 종료시키고 루프 밖으로 나가게 해줍니다.

이 기능들은 예전에 어셈블리 언어에서 많이 사용되었던 `goto`와 비슷한 역할을 하지만, 훨씬 안전하고 관리하기 쉬운 방식으로 구현되어 있어요. 특히, 코드의 가독성과 유지보수성을 높이기 위해 최근 언어 설계에서는 `break`와 `continue`를 적극 활용하도록 권장하고 있답니다.

## 주요 사용법

### 반복문 안에서의 사용

`break`와 `continue`는 `for`, `while`, `do-while` 반복문에서만 사용 가능해요. 

- **continue**: 현재 반복을 건너뛰고 다음 반복으로 바로 돌아갑니다. 예를 들어, 특정 조건을 만족하면 해당 반복을 건너뛰고 다음 값을 처리합니다.
- **break**: 반복문을 즉시 종료하고 루프 밖으로 나갑니다. 특정 조건이 만족되면 반복을 멈추고 프로그램의 다음 부분으로 이동합니다.

#### 예제 코드: `for` 루프에서의 `continue`와 `break`

아래 코드는 `for` 루프를 사용하여 숫자를 리스트에 추가하는 예제예요. 특정 조건이 되면 `continue` 또는 `break`를 사용해 흐름을 조절합니다.

```kotlin
import atomictest.eq

fun main() {
    val nums = mutableListOf<Int>()  // 숫자를 저장할 리스트 초기화

    // 4부터 99까지 4씩 증가하며 반복
    for (i in 4 until 100 step 4) {
        if (i == 8) continue  // 만약 i가 8이면 이 반복 건너뛰기
        // 만약 i가 40이면 루프 종료
        if (i == 40) break
        
        // 그렇지 않으면 숫자를 리스트에 추가
        nums.add(i)
    }

    // 결과 확인
    nums eq "[0, 4, 12, 16, 20, 24, 28, 32, 36]"  // 예상 결과 출력
}
```

#### 설명:
- **continue**: `i == 8`일 때 현재 반복을 건너뛰고 다음 반복으로 돌아갑니다. 그래서 `nums.add(i)`가 실행되지 않는 경우가 있어요.
- **break**: `i == 40`일 때 루프를 즉시 종료하므로 그 이후의 숫자는 리스트에 추가되지 않습니다.

### `while` 루프와 `do-while` 루프에서의 사용

반복문 유형에 상관없이 `break`와 `continue`의 동작 원리는 비슷해요. 아래는 `while` 루프와 `do-while` 루프 예시입니다.

#### `while` 루프 예제

```kotlin
import atomictest.eq

fun main() {
    val nums = mutableListOf<Int>()
    var i = 0

    // i가 100 미만인 동안 반복
    while (i < 100) {
        i += 4  // i를 4씩 증가
        if (i == 8) continue  // 건너뛰기
        if (i == 40) break   // 종료하기
        nums.add(i)          // 그렇지 않으면 추가
    }

    // 결과 확인
    nums eq "[0, 4, 12, 16, 20, 24, 28, 32, 36]"
}
```

#### `do-while` 루프 예제

```kotlin
import atomictest.eq

fun main() {
    val nums = mutableListOf<Int>()
    var i = 0

    // 최소 한 번 실행 후 조건 검사
    do {
        i += 4  // i를 4씩 증가
        if (i == 8) continue  // 건너뛰기
        if (i == 40) break   // 종료하기
        nums.add(i)          // 그렇지 않으면 추가
    } while (i < 100)  // 조건 만족 시 계속 반복

    // 결과 확인
    nums eq "[0, 4, 12, 16, 20, 24, 28, 32, 36]"
}
```

### 레이블 (Labels) 사용

복잡한 중첩 반복문에서 `break`와 `continue`를 특정 범위로 제어하고 싶을 때 레이블을 사용할 수 있어요.

#### 레이블 예제

```kotlin
import atomictest.eq

fun main() {
    val strings = mutableListOf<String>()

    // 외부 반복문 레이블
    outer@ for (c in 'a'..'e') {  // 알파벳 'a'부터 'e'까지 반복
        for (i in 1..9) {         // 숫자 1부터 9까지 반복
            if (i == 5) continue@outer  // 외부 레이블을 사용하여 건너뛰기
            if ("$c$i" == "c3") break@outer  // 외부 레이블로 루프 종료
            strings.add("$c$i")  // 조건에 맞으면 추가
        }
    }

    // 결과 확인
    strings eq listOf("a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", "c1", "c2")
}
```

#### 설명:
- **레이블**: `outer@`를 사용해 외부 반복문으로 제어할 수 있어요. 이로 인해 중첩된 루프에서 더 유연하게 제어가 가능해집니다.

## 핵심 요약

- **`break`**: 반복문을 종료합니다.
- **`continue`**: 현재 반복을 건너뛰고 다음 반복으로 넘어갑니다.
- **적용 범위**: 주로 `for`, `while`, `do-while` 반복문에서 사용됩니다.
- **레이블**: 중첩 반복문에서 특정 루프를 제어하기 위해 사용됩니다.

이러한 기능들은 코드를 더 유연하고 관리하기 쉽게 만들어주지만, 실제로는 Kotlin에서 제공하는 더 높은 수준의 제어 구조를 활용하는 것이 보통 권장됩니다. 그럼에도 불구하고 `break`와 `continue`는 특정 상황에서 유용하게 쓰일 수 있으니 익혀두면 좋습니다!

궁금한 점이 있으면 언제든지 물어보세요! 함께 배우면서 더 나은 Kotlin 개발자가 되어봐요! 😊