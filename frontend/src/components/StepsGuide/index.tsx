import React from "react";
import {
  GuideContainer,
  StepWrapper,
  StepIndicator,
  StepContent,
  StepLine,
  CalloutBox,
  TableWrapper,
  TableHeader,
  TableBody
} from "./styles";

interface StepProps {
  number: number;
  title: string;
  children: React.ReactNode;
}

export const Step: React.FC<StepProps> = ({ number, title, children }) => {
    return (
      <StepWrapper>
        <div className="step-indicator">
          <StepIndicator>{number}</StepIndicator>
          {number >= 1 && <StepLine style={{ height: "100%" }} />} {/* Ajuste para conectar os passos */}
        </div>
        <StepContent>
          <h3>{title}</h3>
          {children}
        </StepContent>
      </StepWrapper>
    );
  };

interface StepsGuideProps {
  children: React.ReactNode;
}

export const StepsGuide: React.FC<StepsGuideProps> = ({ children }) => {
  return <GuideContainer>{children}</GuideContainer>;
};

export const Callout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return <CalloutBox>{children}</CalloutBox>;
};

export const SimpleTable: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return <TableWrapper>{children}</TableWrapper>;
};

export const Header: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return <TableHeader>{children}</TableHeader>;
};

export const Body: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return <TableBody>{children}</TableBody>;
};