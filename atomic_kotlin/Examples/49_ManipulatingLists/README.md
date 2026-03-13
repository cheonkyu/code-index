# 49. 리스트 조작하기: Zip과 Flatten 이해하기

안녕하세요! Kotlin 프로그래밍을 처음 배우는 분들을 위해 오늘은 `zip`과 `flatten`이라는 두 가지 중요한 리스트 조작 기법에 대해 알아보겠습니다. 이 개념들은 코드를 작성할 때 매우 유용하니, 차근차근 따라해보면서 이해해보도록 하죠.

## Zip: 리스트 조합하기

### 기본 개념
`zip`은 두 개의 리스트를 조합해서 새로운 리스트를 만드는 방법입니다. 쉽게 말해, 두 리스트의 각 요소를 짝지어 새로운 쌍을 만드는 거예요. 예를 들어, 옷의 지퍼처럼 각 요소를 연결하는 거죠!

### 예제 코드

```kotlin
// 리스트 zip 예제
fun main() {
    // 리스트 `left`와 `right`를 zip으로 연결
    val left = listOf("a", "b", "c", "d")
    val right = listOf("q", "r", "s", "t")
    
    // `left`와 `right`를 zip하여 쌍 만들기
    val zippedList = left.zip(right)
    println("zippedList: $zippedList") // 출력: [("a", q), ("b", r), ("c", s), ("d", t)]
    
    // 리스트와 범위를 zip하여 연결
    val zippedWithRange = left.zip(0..4)
    println("zippedWithRange: $zippedWithRange") // 출력: [("a", 0), ("b", 1), ("c", 2), ("d", 3)]
    
    // 범위가 더 큰 경우
    val zippedWithRange2 = (10..100).zip(right)
    println("zippedWithRange2: $zippedWithRange2") // 출력: [(10, q), (11, r), (12, s), (13, t)]
}
```

### 추가 작업하기
`zip`으로 생성된 쌍에 대해 추가 작업을 수행할 수도 있어요. 예를 들어, `Person` 객체를 생성하는 경우:

```kotlin
// Pair로 객체 생성하기
package manipulatinglists
import atomictest.eq

data class Person(val name: String, val id: Int)

fun main() {
    val names = listOf("Bob", "Jill", "Jim")
    val ids = listOf(1731, 9274, 8378)
    
    val persons = names.zip(ids) { name, id -> Person(name, id) }
    println("persons: $persons") // 출력: [Person(name=Bob, id=1731), Person(name=Jill, id=9274), Person(name=Jim, id=8378)]
}
```

### 인접 요소 조합하기
리스트의 인접한 요소들을 짝지어 쌍으로 만드는 경우에는 `zipWithNext`를 사용할 수 있어요:

```kotlin
// 인접 요소 짝지어 만들기
fun main() {
    val list = listOf('a', 'b', 'c', 'd')
    val zippedList = list.zipWithNext()
    println("zipWithNext 결과: $zippedList") // 출력: [Pair(a, b), Pair(b, c), Pair(c, d)]
    
    // 추가 작업 수행
    val combinedList = list.zipWithNext { a, b -> "$a$b" }
    println("결합 결과: $combinedList") // 출력: [ab, bc, cd]
}
```

## Flatten: 중첩 리스트 평평하게 만들기

### 기본 개념
`flatten`은 중첩된 리스트를 하나의 평평한 리스트로 변환해주는 기능입니다. 여러 개의 리스트가 중첩되어 있을 때 이를 단일 리스트로 만드는 데 사용됩니다.

### 예제 코드

```kotlin
// 중첩 리스트 평평하게 만들기
fun main() {
    val nestedList = listOf(
        listOf(1, 2),
        listOf(4, 5),
        listOf(7, 8)
    )
    val flattenedList = nestedList.flatten()
    println("평평화된 리스트: $flattenedList") // 출력: [1, 2, 4, 5, 7, 8]
}
```

### `flatMap` 이해하기
`flatMap`은 `map`과 `flatten`을 한 번에 수행하는 편리한 기능입니다. 중첩된 리스트에서 모든 가능한 조합을 생성하고 싶을 때 유용해요.

```kotlin
// flatMap으로 모든 조합 생성하기
fun main() {
    val intRange = 1..3
    
    // map을 사용해 중첩 리스트 생성
    val nestedCombinations = intRange.map { a ->
        intRange.map { b -> a to b }
    }
    println("중첩 리스트: $nestedCombinations") // 출력: [[(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)], [(3, 1), (3, 2), (3, 3)]]
    
    // flatten으로 평평하게 만들기
    val flattenedCombinations = nestedCombinations.flatten()
    println("평평화된 조합: $flattenedCombinations") // 출력: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    
    // flatMap으로 한 번에 처리하기
    val flatMapResult = intRange.flatMap { a ->
        intRange.map { b -> a to b }
    }
    println("flatMap 결과: $flatMapResult") // 출력: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
}
```

## 주요 개념 요약
- **`zip`**: 두 리스트의 요소를 짝지어 새로운 쌍의 리스트를 만듭니다. 추가 작업을 수행할 수도 있어요.
- **`zipWithNext`**: 단일 리스트의 인접한 요소들을 짝지어 쌍을 만듭니다.
- **`flatten`**: 중첩된 리스트를 하나의 평평한 리스트로 변환합니다.
- **`flatMap`**: `map`과 `flatten`을 한 번에 수행해 중첩된 리스트에서 모든 조합을 생성합니다.

이제 기본적인 개념을 이해하셨나요? 연습을 통해 더 익숙해질 수 있으니, 다양한 예제를 시도해보세요! 궁금한 점이 있으면 언제든지 물어보세요. 행운을 빕니다!