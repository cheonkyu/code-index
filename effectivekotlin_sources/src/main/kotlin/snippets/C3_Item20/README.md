# Item 20: 자주 사용되는 알고리즘을 중복 작성하지 않기

## 핵심 가이드라인

이 섹션에서는 코드 내에서 자주 사용되는 알고리즘을 한 번만 구현하고 재사용하는 방법을 강조합니다. 중복된 코드 작성은 유지보수를 어렵게 만들고 버그 수정이나 기능 확장 시 오류를 유발할 가능성을 높입니다. 따라서, 공통적으로 사용되는 알고리즘은 클래스나 유틸리티 함수 내에서 한 번 정의하고 필요한 곳마다 호출하거나 인스턴스화하여 사용하는 것이 좋습니다.

### 이유 (Best Practice)
- **유지보수성 향상**: 중복 코드를 제거하면 버그 수정이나 기능 개선이 훨씬 쉽고 빠릅니다.
- **코드 일관성 유지**: 동일한 알고리즘이 여러 곳에서 일관된 방식으로 구현되므로 코드의 일관성이 유지됩니다.
- **효율성 증대**: 알고리즘이 한 곳에 모여 있으므로 메모리 사용과 실행 효율성이 향상됩니다.

## 예제 코드

다음은 리스트에서 특정 조건을 만족하는 요소를 찾는 알고리즘을 한 번만 정의하고 여러 곳에서 재사용하는 예시입니다.

```kotlin
// 유틸리티 함수로 알고리즘 정의
fun <T> findFirstMatching(list: List<T>, predicate: (T) -> Boolean): T? {
    return list.firstOrNull { predicate(it) }
}

// 사용 예시 1: 나이가 18세 이상인 첫 번째 사용자 찾기
data class User(val name: String, val age: Int)
val users = listOf(User("Alice", 25), User("Bob", 17), User("Charlie", 30))
val adultUser = findFirstMatching(users) { user -> user.age >= 18 }
println("성인 사용자: $adultUser")  // 성인 사용자: User(name='Alice', age=25)

// 사용 예시 2: 특정 문자열 길이 이상인 요소 찾기
val items = listOf("apple", "banana", "cherry", "date")
val longWords = findFirstMatching(items) { word -> word.length > 5 }
println("길이가 5글자 이상인 단어: $longWords")  // 길이가 5글자 이상인 단어: cherry
```

## 핵심 요약
- 자주 사용되는 알고리즘은 한 곳에서 정의하고 재사용합니다.
- 중복 코드 제거로 유지보수와 효율성이 향상됩니다.
- 일관된 코드 구현으로 팀 작업 시 혼란을 줄입니다.