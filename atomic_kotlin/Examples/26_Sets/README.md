# 26. Sets (집합)

안녕하세요! 코틀린 프로그래밍을 배우는 초보자 여러분, 오늘은 코틀린에서 정말 유용한 자료구조 중 하나인 **집합 (Set)**에 대해 배워볼게요. 집합은 중복을 허용하지 않고, 특정 요소들의 모임을 표현하는 데 사용됩니다. 이해하기 쉽게 단계별로 설명해 드릴게요.

## 핵심 개념 요약

1. **중복 제거**: 집합에 동일한 요소를 여러 번 추가해도, 결국 한 번만 저장됩니다.
2. **요소 순서 무관**: 집합 내 요소의 순서는 중요하지 않아요. `{1, 2}`와 `{2, 1}`은 동일한 집합으로 간주됩니다.
3. **멤버십 확인**: `in` 연산자나 `contains()` 메서드를 사용해 요소가 집합에 있는지 쉽게 확인할 수 있어요.
4. **집합 연산**: 집합 간의 합집합(`union`), 교집합(`intersect`), 차집합(`subtract`) 등 다양한 연산이 가능합니다.
5. **생성 방법**:
   - **읽기 전용 집합**: `setOf()` 사용 (예: `setOf(1, 2, 3)`)
   - **변경 가능 집합**: `mutableSetOf()` 사용 (예: `mutableSetOf<Int>()`)

### 예제 코드 설명

#### 중복 제거와 집합 생성

```kotlin
import atomictest.eq // 테스트 라이브러리

fun main() {
    // 리스트에서 중복 제거하기
    val list = listOf(3, 3, 2, 1, 2)
    val uniqueList = list.toSet() // 중복 제거된 집합
    println(uniqueList eq setOf(1, 2, 3)) // 출력: true

    // 문자열의 고유 문자 집합 생성
    val chars = "abbcc".toSet() // 고유 문자 집합
    println(chars eq setOf('a', 'b', 'c')) // 출력: true

    // 리스트에서 중복 제거 (리스트 형태로 반환)
    val distinctList = list.distinct() // 중복 제거된 리스트
    println(distinctList eq listOf(3, 2, 1)) // 출력: true
}
```

**해설**:
- `list.toSet()`를 사용하면 리스트에서 중복 요소가 제거된 집합이 생성됩니다.
- 문자열 `"abbcc"`는 고유한 문자 집합 `{'a', 'b', 'c'}`로 변환됩니다.
- `distinct()` 메서드는 중복을 제거한 새로운 리스트를 반환합니다.

#### 집합 연산 예제

```kotlin
fun main() {
    val intSet = setOf(1, 1, 2, 3, 9, 9, 4) // 중복 제거된 집합

    // 요소 존재 확인
    println((9 in intSet) eq true) // 출력: true
    println((99 in intSet) eq false) // 출력: true

    // 멤버십 확인 메서드 사용
    println(intSet.contains(9)) // 출력: true
    println(intSet.contains(99)) // 출력: false

    // 집합 연산 예제
    val unionSet = intSet.union(setOf(3, 4, 5, 6)) // 합집합
    println(unionSet eq setOf(1, 2, 3, 4, 5, 6, 9)) // 출력: true

    val intersectSet = intSet intersect setOf(0, 1, 2, 7, 8) // 교집합
    println(intersectSet eq setOf(1, 2)) // 출력: true

    val diffSet = intSet subtract setOf(0, 1, 9, 10) // 차집합
    println(diffSet eq setOf(2, 3, 4)) // 출력: true
    println(intSet - setOf(0, 1, 9, 10) eq setOf(2, 3, 4)) // 출력: true
}
```

**해설**:
- `union()` 메서드는 두 집합의 합집합을 반환합니다.
- `intersect()` 메서드는 두 집합의 교집합을 반환합니다.
- `subtract()` 또는 `-` 연산자는 차집합을 생성합니다.

#### 집합 생성 (읽기 전용 vs 변경 가능)

```kotlin
import atomictest.eq

fun main() {
    // 읽기 전용 집합 생성
    val readOnlySet = setOf(42) // 기본적으로 읽기 전용
    readOnlySet += 42 // 추가해도 동작하지 않음
    println(readOnlySet eq setOf(42)) // 출력: true

    // 변경 가능 집합 생성
    val mutableSet = mutableSetOf<Int>()
    mutableSet += 42
    mutableSet += 42 // 중복 추가해도 하나만 유지
    println(mutableSet eq setOf(42)) // 출력: true
    mutableSet -= 42
    println(mutableSet eq setOf<Int>()) // 출력: true
}
```

**해설**:
- `setOf()`로 생성된 집합은 기본적으로 읽기 전용입니다.
- `mutableSetOf()`로 생성하면 요소를 추가하거나 제거할 수 있습니다.

## 간단한 연습 문제

1. 주어진 리스트 `[5, 5, 3, 2, 3]`을 집합으로 변환해 보세요.
2. `{1, 2, 3}` 집합과 `{3, 4, 5}` 집합의 합집합과 교집합을 구해보세요.
3. `setOf("apple", "banana", "apple")`을 생성하고 중복을 제거한 결과를 확인해보세요.

이 내용을 통해 코틀린에서 집합을 어떻게 활용하는지 조금 더 이해하셨길 바라요! 더 궁금한 점이 있으면 언제든지 물어봐 주세요. 함께 공부해요! 🚀