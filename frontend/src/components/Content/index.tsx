import React from "react";
import { ContentStyle } from "./styles";
import { useMenu } from "../../contexts/MenuContext";
import Breadcrumb from '../Breadcrumb';

export const Content = (props) => {
  const { isCollapsed } = useMenu();

  return (
    <ContentStyle isCollapsed={isCollapsed}>
        <Breadcrumb />
        {props.children}
    </ContentStyle>
  );
};