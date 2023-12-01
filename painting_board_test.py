from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
from PyQt5.QtGui import QPainterPath, QColor, QPen
import json
import sys


def save_curve_data(scene):
    curve_data = []

    for item in scene.items():
        if hasattr(item, 'path') and isinstance(item.pen(), QPen):  # QPainterPath를 가진 아이템만 추출
            path = item.path()  # 곡선의 QPainterPath 가져오기

            # QPainterPath의 점들을 리스트로 변환하여 저장
            curve_points = []
            for i in range(path.elementCount()):
                element = path.elementAt(i)
                curve_points.append({'x': element.x, 'y': element.y})

            # 곡선 데이터에 추가
            curve_data.append({
                'points': curve_points,
                'pen_color': item.pen().color().name(),
                'pen_width': item.pen().width()
                # 다른 속성들을 필요한 경우 추가
            })

    with open('curve_data.json', 'w') as file:
        json.dump(curve_data, file)


def load_curve_data(scene):
    # with open('curve_data.json', 'r') as file:
    with open('saved_drawing.json', 'r') as file:
        loaded_data = json.load(file)

    for curve_item in loaded_data:
        path = QPainterPath()

        for index in range(len(curve_item['points'])):
            if index == 0:
                continue
            path.moveTo(curve_item['points'][index-1]['x'], curve_item['points'][index-1]['y'])
            path.lineTo(curve_item['points'][index]['x'], curve_item['points'][index]['y'])

        # for point in curve_item['points']:
        #     path.moveTo(point['x'], point['y'])
        #     path.lineTo(point['x'], point['y'])
            # path.moveTo(point['x'], point['y'])

        pen = QPen(QColor(curve_item['pen_color']))
        pen.setWidth(curve_item['pen_width'])

        curve = scene.addPath(path, pen)



app = QApplication(sys.argv)
# QGraphicsScene 생성
scene = QGraphicsScene()

view = QGraphicsView(scene)


view.show()
# # 데이터 불러오기
load_curve_data(scene)

# 곡선 그리기
# path = QPainterPath()
# path.moveTo(10, 10)
# path.cubicTo(80, 80, 180, 80, 250, 10)  # 곡선 그리기 예시
#
# pen = QPen(QColor('red'))
# pen.setWidth(2)
# curve_item = scene.addPath(path, pen)
#
# # 데이터 저장
# save_curve_data(scene)
#


sys.exit(app.exec_())
