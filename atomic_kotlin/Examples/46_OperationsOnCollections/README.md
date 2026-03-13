# 46. 컬렉션 연산하기 (OperationsOnCollections)

안녕하세요! 코틀린 프로그래밍을 처음 접하시는 분들을 위해 이번 챕터에서는 컬렉션에 대한 다양한 연산 방법들을 쉽게 설명해드릴게요. 코틀린은 강력한 컬렉션 처리 기능을 제공해서 코드를 간결하고 효율적으로 만들 수 있답니다. 이번 주제에서는 리스트 생성부터 여러 가지 필터링 및 탐색 연산까지 알아볼게요. 차근차근 따라와 보세요!

## 리스트 생성하기

코틀린에서 리스트를 만드는 방법이 몇 가지 있어요. 특히 람다(lambda)를 사용하면 쉽게 초기값 리스트를 만들 수 있어요.

### 리스트 기본 생성 예제

```kotlin
import atomictest.eq // 테스트를 위한 라이브러리로 가정합니다.

fun main() {
    // 기본 인덱스를 사용해 숫자 리스트 생성
    val list1 = List(10) { it } // 0부터 시작해서 0, 1, 2, ..., 9까지의 리스트
    println(list1) // 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    // 모든 요소가 동일한 값으로 초기화된 리스트
    val list2 = List(10) { 0 } // 모든 요소가 0인 리스트
    println(list2) // 출력: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    // 문자 리스트 생성 예제
    val list3 = List(10) { 'a' + it } // 'a'부터 시작해서 순서대로 문자 리스트 생성
    println(list3) // 출력: [a, b, c, d, e, f, g, h, i, j]

    // 순환 리스트 생성 예제
    val list4 = List(10) { list3[it % 3] } // 리스트의 첫 3개 요소를 순환하며 생성
    println(list4) // 출력: [a, b, c, a, b, c, a, b, c, a]
}
```

### 뮤테이블 리스트 생성 예제

뮤테이블 리스트도 비슷한 방식으로 생성할 수 있어요. 람다를 리스트 생성 인자로 사용할 수 있어요.

```kotlin
import atomictest.eq // 테스트를 위한 라이브러리로 가정합니다.

fun main() {
    // 람다를 리스트 생성 인자로 사용한 뮤테이블 리스트 생성
    val mutableList1 = MutableList(5) { 10 * (it + 1) } // 인덱스에 따라 값을 계산해 리스트 생성
    println(mutableList1) // 출력: [10, 20, 30, 40, 50]

    // 람다 분리해서 사용하기
    val mutableList2 = MutableList(5) { 10 * (it + 1) } // 람다를 분리해서 사용해도 결과는 같음
    println(mutableList2) // 출력: [10, 20, 30, 40, 50]
}
```

## 필터링 및 탐색 연산

컬렉션에서 특정 조건에 맞는 요소들을 찾거나 필터링하는 연산들이 매우 유용해요. 여기 몇 가지 중요한 연산들을 살펴볼게요.

### 필터링과 탐색 함수 예제

```kotlin
import atomictest.eq // 테스트를 위한 라이브러리로 가정합니다.

fun main() {
    val list = listOf(-3, -1, 5, 7, 10) // 테스트할 리스트

    // 조건에 맞는 요소만 필터링
    println(list.filter { it > 0 }) // 출력: [5, 7, 10]

    // 조건에 맞는 요소의 개수 세기
    println(list.count { it > 0 }) // 출력: 3

    // 조건에 맞는 첫 번째 요소 찾기
    println(list.find { it > 0 }) // 출력: 5
    println(list.firstOrNull { it > 0 }) // 출력: 5

    // 마지막 요소 찾기
    println(list.lastOrNull { it < 0 }) // 출력: -1

    // 조건에 맞는 요소가 있는지 확인
    println(list.any { it > 0 }) // 출력: true
    println(list.any { it != 0 }) // 출력: true

    // 모든 요소가 조건에 맞는지 확인
    println(list.all { it > 0 }) // 출력: false
    println(list.all { it != 0 }) // 출력: true

    // 조건에 맞지 않는 요소들만 필터링
    println(list.filterNot { it > 0 }) // 출력: [-3, -1]
}
```

### `partition()` 함수로 두 그룹 나누기

`partition()` 함수는 리스트를 두 그룹으로 나눌 수 있어요. 조건에 맞는 요소와 그렇지 않은 요소를 각각의 리스트로 반환합니다.

```kotlin
import atomictest.eq // 테스트를 위한 라이브러리로 가정합니다.

fun main() {
    val list = listOf(-3, -1, 5, 7, 10) // 테스트할 리스트
    val isPositive = { i: Int -> i > 0 } // 조건 함수 정의

    // 필터링과 partition() 함께 사용하기
    println(list.filter(isPositive)) // 출력: [5, 7, 10]
    println(list.filterNot(isPositive)) // 출력: [-3, -1]

    // partition() 함수로 두 그룹 나누기
    val (pos, neg) = list.partition { it > 0 }
    println(pos) // 출력: [5, 7, 10]
    println(neg) // 출력: [-3, -1]
}
```

### 주요 개념 요약

1. **리스트 생성**: `List(크기) { 람다 표현식 }`으로 쉽게 초기화 가능해요. 뮤테이블 리스트도 비슷한 방식으로 생성할 수 있어요.
2. **필터링 연산**:
   - `filter()`: 조건에 맞는 요소들로 새로운 리스트 생성
   - `count()`: 조건에 맞는 요소 개수 세기
   - `find()`, `firstOrNull()`: 첫 번째 조건에 맞는 요소 찾기
   - `lastOrNull()`: 마지막 조건에 맞는 요소 찾기
   - `any()`, `all()`: 조건에 대한 전체 리스트의 일치 여부 확인
3. **반대로 필터링**: `filterNot()`으로 조건에 맞지 않는 요소들만 추출 가능해요.
4. **partition()**: 리스트를 조건에 맞는 요소와 그렇지 않은 요소로 나누어 두 개의 리스트로 반환합니다.

이렇게 다양한 기능들을 활용하면 코틀린 컬렉션 처리가 훨씬 쉬워질 거예요. 연습을 많이 하면 더 자연스럽게 사용할 수 있을 거에요! 질문이 있으면 언제든지 물어보세요! 😊