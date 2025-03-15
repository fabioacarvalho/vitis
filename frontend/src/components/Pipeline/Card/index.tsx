import React, { useRef, useContext } from "react";
import { useDrag, useDrop } from 'react-dnd';

import BoardContext from '../Board/context';

import { Container, Label } from "./styles";

export default function Card({ data, index, listIndex }) {
    const ref = useRef();
    const { move } = useContext(BoardContext)

    const [{ isDragging }, dragRef] = useDrag({
        type: 'CARD',
        item: { id: data.id, index: index, content: data.content, listIndex: listIndex },
        collect: monitor => ({
          isDragging: monitor.isDragging(),
        }),
    });

    const [, dropRef] = useDrop({
        accept: 'CARD',
        hover(item, monitor){
            const draggedListIndex = item.listIndex;
            const targetListIndex = listIndex;

            const draggedIndex = item.index;
            const targetIndex = index;

            if(draggedIndex == targetIndex && draggedListIndex == targetListIndex) {
                return;
            };

            const targetSize = ref.current.getBoundingClientRect();
            const targetPointCenter = (targetSize.bottom - targetSize.top) / 2;

            const draggedOffset = monitor.getClientOffset();
            const draggedTop = draggedOffset.y - targetSize.top;


            if(draggedIndex < targetIndex && draggedTop < targetPointCenter) {
                return;
            };

            if(draggedIndex > targetIndex && draggedTop > targetPointCenter) {
                return;
            };

            move(draggedListIndex, targetListIndex, draggedIndex, targetIndex);

            item.index = targetIndex;
            item.listIndex = targetListIndex;

        }
    })

    dragRef(dropRef(ref));

    return (
        <Container isDragging={isDragging} ref={ref}>
            <header>
                { data.labels.map(label => <Label key={label} color={label} />) }
            </header>
            <p>{ data.content }</p>
            { data.user && (<img src={data.user} alt="" />)}
        </Container>
    );
}