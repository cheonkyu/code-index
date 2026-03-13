# 50. BuildingMaps: 맵을 활용한 데이터 그룹화

안녕하세요! 이번 챕터에서는 코틀린 프로그래밍에서 매우 유용한 자료구조인 `맵(Map)`을 배워볼게요. 맵은 특정 키를 이용해 빠르게 값에 접근할 수 있게 해주는 도구죠. 이번 단원에서는 `맵`을 이용해 데이터를 그룹화하는 다양한 방법들을 배워볼게요. 초보자분들도 쉽게 이해할 수 있도록 단계별로 설명해볼게요.

## 1. 데이터 리스트로부터 맵 생성하기

먼저, 사람들의 이름과 나이 정보를 리스트로 가지고 있다고 가정해볼게요. 이 정보를 이용해 맵을 만드는 방법을 알아볼게요.

### 예제 코드

```kotlin
package buildingmaps

data class Person(
    val name: String,  // 이름
    val age: Int       // 나이
)

fun main() {
    // 이름과 나이 리스트
    val names = listOf("Alice", "Arthricia", "Bob", "Bill", "Birdperson", "Charlie", "Crocubot", "Franz", "Revolio")
    val ages = listOf(21, 15, 25, 25, 42, 21, 42, 21, 33)

    // 리스트를 묶어서 Person 객체 리스트 생성
    val peopleList = names.zip(ages) { name, age -> Person(name, age) }

    // 나이를 키로 하는 맵 생성
    val ageMap = peopleList.groupBy({ person -> person.age }, { person -> person })

    // 출력 확인
    for ((age, people) in ageMap) {
        println("나이 $age: $people")
    }
}
```

### 설명
- **`data class Person`**: 이름과 나이를 저장할 데이터 클래스를 정의했어요.
- **`zip` 함수**: 두 리스트를 묶어서 `Person` 객체 리스트를 만드는 데 사용했어요. 각 이름과 나이를 쌍으로 묶어 `Person` 객체를 생성해요.
- **`groupBy` 함수**: `groupBy` 함수는 주어진 키를 기준으로 데이터를 그룹화해줘요. 여기서는 나이(`age`)를 키로 사용해서 각 나이대의 사람들을 그룹화해요.

## 2. `groupBy()` vs `filter()`

`groupBy()`와 `filter()`를 사용해서 동일한 결과를 얻는 방법을 비교해볼게요. `groupBy()`가 더 효율적이라는 점을 강조할게요.

### `groupBy()` 예제

```kotlin
// 나이로 그룹화
val ageGroupMap = peopleList.groupBy({ person -> person.name.first() }, { person -> person })
println(ageGroupMap)  // 이름의 첫 글자를 키로 그룹화 결과 출력
```

### `filter()` 예제 (반복 필요)

```kotlin
// 첫 글자가 'A'인 사람 필터링
val filteredByA = peopleList.filter { it.name.first() == 'A' }
println(filteredByA)

// 첫 글자가 'F'인 사람 필터링 (반복 필요)
val filteredByF = peopleList.filter { it.name.first() == 'F' }
println(filteredByF)
```

### 설명
- **`groupBy()`**: 키를 기준으로 한 번에 그룹화를 수행해요. 효율적이고 간결해요.
- **`filter()`**: 특정 조건에 맞는 요소만 선택하지만, 각 조건마다 반복적으로 필터링해야 해요. 이는 효율성이 떨어지므로, 여러 그룹을 만들 때는 `groupBy()`가 더 좋아요.

## 3. `associateWith()`와 `associateBy()`

다른 맵 생성 방법들도 알아볼게요. 특히 `associateWith()`와 `associateBy()`는 특정 조건에 따라 맵을 만들 때 유용해요.

### `associateWith()` 예제

```kotlin
import kotlin.collections.MapEntry

val nameMap = peopleList.associateWith { it.name }
println(nameMap)  // 이름을 키로 맵 생성
```

### `associateBy()` 예제

```kotlin
val reverseNameMap = peopleList.associateBy { it.name }
println(reverseNameMap)  // 이름을 키로 맵 생성, 순서 반대로
```

### 설명
- **`associateWith()`**: 주어진 함수를 통해 키를 생성해요. 여기서는 각 `Person` 객체의 이름을 키로 사용해요.
- **`associateBy()`**: `associateWith()`와 유사하지만, 키와 값의 역할을 바꾸어 생성해요. 즉, 이름을 키로 하고 `Person` 객체를 값으로 맵을 만드는 거죠.

## 주요 핵심 개념 요약

1. **`groupBy()`**: 주어진 키를 기준으로 데이터를 그룹화해요. 여러 그룹을 한 번에 만들 수 있어 효율적이에요.
2. **`filter()`**: 조건에 맞는 요소를 필터링해요. 반복적인 필터링이 필요할 때는 효율성이 떨어질 수 있어요.
3. **`associateWith()`**: 주어진 함수로 키를 생성하여 맵을 만드는 방법이에요.
4. **`associateBy()`**: 키와 값의 역할을 바꾸어 맵을 만드는 방법이에요.

이렇게 맵을 활용하면 데이터를 빠르고 효과적으로 관리할 수 있어요. 코틀린에서 맵을 다루는 방법을 익혀두면 많은 도움이 될 거예요! 궁금한 점이 있으면 언제든지 물어봐 주세요!