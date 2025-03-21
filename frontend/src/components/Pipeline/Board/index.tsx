import React, { useState } from "react";
import { produce } from "immer";
import loadLists from "./default";

import BoardContext from './context'

import List from "../List";

import { Container } from "./styles";

const data = loadLists()

export default function Board() {
    const [lists, setLists] = useState(data)

    const move = (fromList: any, toList: any, from: any, to: any) => {
        setLists(produce((lists: any, draft: any) => {
            const dragged = draft[fromList].cards[from]
            draft[fromList].cards.splice(from, 1)
            draft[toList].cards.splice(to, 0, dragged)
        }))
    }

    return (
        <BoardContext.Provider value={{ lists, move }}>
            <Container>
                {
                    lists.map((list: any, index: number) => <List key={list.title} index={index} data={list} />)
                }
            </Container>
        </BoardContext.Provider>
    );
}