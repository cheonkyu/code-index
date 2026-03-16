# Item 45: 불필요한 객체 생성 피하기

## 핵심 가이드라인 및 이유 (Best Practice)

프로그램에서 객체를 생성할 때마다 메모리 사용량이 증가하고, 때때로 성능 저하가 발생할 수 있습니다. 특히 반복적인 작업이나 루프 내부에서 과도한 객체 생성은 자원 소모를 크게 증가시킵니다. 따라서 효율적인 코드 작성을 위해 불필요한 객체 생성을 최소화하는 것이 중요합니다.

### 주요 가이드라인:
1. **불필요한 객체 생성 방지**: 반복적인 연산 내에서 자주 생성되는 객체를 최소화하거나 재사용합니다.
2. **스태틱 메서드 활용**: 특정 작업이 필요할 때마다 객체를 생성하는 대신 스태틱 메서드를 활용하여 성능을 개선합니다.
3. **루프 내 객체 생성 주의**: 루프 내부에서 객체를 생성할 때는 그 필요성을 반드시 검토하고, 가능하다면 외부에서 미리 생성하여 사용합니다.

### 이유:
- **메모리 효율성**: 객체 생성은 메모리 할당을 필요로 하므로, 불필요한 생성은 메모리 사용량을 증가시킵니다.
- **성능 향상**: 객체 생성은 시간이 소요되는 작업이므로, 이를 줄이면 프로그램의 실행 속도가 향상됩니다.
- **코드 가독성**: 불필요한 객체 생성을 제거하면 코드가 더 간결하고 이해하기 쉬워집니다.

## 예제 코드

### 불필요한 객체 생성 예제 (피해야 할 방식)
```kotlin
fun processItems(items: List<Item>) {
    for (item in items) {
        val transformedItem = item.transform()  // 매번 반복마다 새로운 객체 생성
        // 처리 로직
    }
}
```

### 개선된 코드 (효율적인 방식)
```kotlin
fun processItems(items: List<Item>) {
    for (item in items) {
        val transformedItem = item.transform()  // 단 한 번만 생성 후 재사용
        // 만약 필요하다면, 루프 외부에서 미리 생성하여 사용
        val reusableTransformer = ItemTransformer()  // 외부에서 미리 생성
        val transformedItemByTransformer = reusableTransformer.transform(item)
        // 처리 로직
    }
}

// 또는 스태틱 메서드 활용 예시
class ItemTransformer {
    companion object {
        fun transform(item: Item): Item {
            // 객체 생성 로직
            return item.copy(// 예시 로직)
        }
    }
}
```

## 핵심 요약
- 불필요한 객체 생성을 줄여 메모리와 성능을 최적화합니다.
- 루프 내부에서 객체 생성 시 신중하게 검토하고 필요에 따라 외부에서 미리 생성합니다.
- 스태틱 메서드 활용으로 효율적인 객체 관리를 실현합니다.