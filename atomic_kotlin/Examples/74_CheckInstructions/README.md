# 74. CheckInstructions: 함수 조건 검사하기

안녕하세요! 이번 챕터에서는 코틀린에서 함수의 조건을 검사하는 방법에 대해 배워볼게요. 특히 `require()` 함수를 활용하는 방법에 대해 알아보겠습니다. 초보자분들도 쉽게 이해할 수 있도록 차근차근 설명해드릴게요.

## 무엇이 필요한가요?

함수에서 입력값이 올바르고 결과가 예상대로 나오는지 확인하는 것이 중요해요. 이를 위해 `require()` 함수를 사용하면 코드를 더 명확하고 유지보수하기 쉽게 만들 수 있어요. `require()`는 함수 시작 부분이나 결과 검증 시 사용하면 좋답니다.

### 주요 핵심 개념

1. **함수 시작 부분 검사**: 함수 인자가 올바른 범위나 타입인지 확인합니다.
2. **결과 검증**: 함수의 계산 결과가 예상대로 나왔는지 확인합니다.
3. **예외 처리**: 조건이 맞지 않으면 `IllegalArgumentException`을 던집니다.
4. **문서화 역할**: 코드를 읽는 사람들에게 함수의 요구사항을 명확히 알려줍니다.

---

### 예제 1: 월 범위 검사하기

먼저, `JulianMonth` 클래스를 살펴보겠습니다. 이 클래스는 월의 범위를 검사하는 예시예요.

```kotlin
package checkinstructions

import atomictest.*

data class Month(val monthNumber: Int) {
    init {
        // 월은 항상 1부터 12 사이여야 합니다.
        require(monthNumber in 1..12) {
            "월 범위 오류: $monthNumber (월은 1부터 12 사이여야 합니다)"
        }
    }
}

fun main() {
    // 올바른 월 생성
    val month1 = Month(1)
    println("Month(monthNumber=1)")  // 출력: Month(monthNumber=1)

    // 범위를 벗어난 월 생성 (에러 발생 예상)
    capture { Month(13) } eq "IllegalArgumentException: 월 범위 오류: 13 (월은 1부터 12 사이여야 합니다)"
}
```

**설명**:
- `require()`는 `monthNumber`가 1부터 12 사이인지 확인합니다.
- 범위를 벗어나면 `IllegalArgumentException`을 던지고 오류 메시지를 함께 출력합니다.

### 예제 2: 이차방정식 해 구하기 (조건 검사 활용)

다음으로, 이차방정식의 해를 구하는 함수 `quadraticZeroes`를 살펴볼게요. `require()`를 사용해 입력값 조건을 검사합니다.

```kotlin
package checkinstructions

import kotlin.math.sqrt
import atomictest.*

class Roots(val root1: Double, val root2: Double)

fun quadraticZeroes(
    a: Double,
    b: Double,
    c: Double
): Roots {
    // 계수 `a`가 0이면 에러
    require(a != 0.0) { "계수 a가 0입니다" }

    // 판별식 `underRadical`이 음수가 아닌지 확인
    val underRadical = b * b - 4 * a * c
    require(underRadical >= 0) { "음수 판별식: $underRadical" }

    val squareRoot = sqrt(underRadical)
    val root1 = (-b - squareRoot) / 2 * a
    val root2 = (-b + squareRoot) / 2 * a
    return Roots(root1, root2)
}

fun main() {
    // 잘못된 입력 예시
    capture { quadraticZeroes(0.0, 4.0, 5.0) } eq "IllegalArgumentException: 계수 a가 0입니다"
    
    // 잘못된 판별식 예시
    capture { quadraticZeroes(3.0, 4.0, 5.0) } eq "IllegalArgumentException: 음수 판별식: -44.0"

    // 올바른 입력 예시
    val roots = quadraticZeroes(3.0, 8.0, 5.0)
    roots.root1 eq -15.0  // 출력: true
    roots.root2 eq -9.0   // 출력: true
}
```

**설명**:
- `require()`를 사용해 `a`가 0이 아닌지, 판별식 `underRadical`이 음수가 아닌지 검사합니다.
- 이렇게 하면 함수의 입력 조건을 명확하게 보장하고 코드가 더 읽기 쉬워집니다.

### 예제 3: 파일 작업을 위한 `DataFile` 클래스

`DataFile` 클래스는 파일 입출력 작업을 간편하게 처리해줍니다.

```kotlin
package checkinstructions

import atomictest.eq
import java.io.File
import java.nio.file.Paths

val targetDir = File("DataFiles")

class DataFile(val fileName: String) : File(targetDir, fileName) {
    init {
        if (!targetDir.exists()) {
            targetDir.mkdir()
        }
    }

    fun erase() { if (exists()) delete() }
    fun reset(): File {
        erase()
        createNewFile()
        return this
    }
}

fun main() {
    val dataFile = DataFile("Test.txt")
    dataFile.reset() eq Paths.get("DataFiles", "Test.txt").toString()
}
```

**설명**:
- `DataFile` 클래스는 파일이 `DataFiles` 디렉토리 내에 위치하도록 보장합니다.
- `reset()` 메서드를 사용하면 파일을 지우고 새로 생성할 수 있어요.

---

**요약**

- `require()` 함수는 함수 인자나 결과의 유효성을 검사합니다.
- 이를 통해 코드의 가독성을 높이고 오류를 미리 찾아낼 수 있어요.
- `require()`는 코드를 더 명확하게 만들고 유지보수하기 쉽게 도와줍니다.

이제 코틀린에서 `require()`를 어떻게 사용하는지 좀 더 이해하셨길 바랍니다! 연습해보면서 점점 익숙해질 거예요. 궁금한 점이 있으면 언제든지 물어보세요!