"""Задача о рюкзаке:
Первая строка содержит количество предметов, и вместимость рюкзака. Каждая из следующих n строк задаёт стоимость и объем предмета.
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой."""

n, w = map(int, input().split())
sum_things, w_things, things = 0, 0, []

for _ in range(n):
    thing = tuple(map(int, input().split()))
    things.append(thing)
things.sort(key=lambda cost_weight: cost_weight[0] / cost_weight[1], reverse=True)

for i in range(n):
    if things[i][1] <= w - w_things:
        sum_things += things[i][0]
        w_things += things[i][1]
    else:
        while w - w_things != 0:
            sum_things += (things[i][0] / things[i][1])
            w_things += 1
print('{:.3f}'.format(sum_things))
