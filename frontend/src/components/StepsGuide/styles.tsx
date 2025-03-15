import styled from "styled-components";

export const GuideContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: start;
  gap: 16px;
  position: relative;
`;

export const StepWrapper = styled.div`
  display: flex;
  align-items: flex-start;
  gap: 16px;
  position: relative;
`;

export const StepIndicator = styled.div`
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  background-color: #007bff;
  color: white;
  border-radius: 50%;
  position: relative;
  z-index: 2;
`;

export const StepLine = styled.div`
  position: absolute;
  width: 2px;
  background-color: #ccc;
  top: 10px;
  left: 20px;
  transform: translateX(-50%);
  z-index: 1;
`;

export const StepContent = styled.div`
  margin-left: 16px;
  flex: 1;
  
  h3 {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  p, ul {
    margin-top: 4px;
  }

  img {
    max-width: 100%;
    border-radius: 8px;
  }
`;

export const CalloutBox = styled.div`
  background-color: #f8f9fa;
  padding: 12px;
  border-left: 4px solid #007bff;
  margin-top: 8px;
  border-radius: 4px;
`;

export const TableWrapper = styled.table`
  width: 100%;
  border-collapse: collapse;
  margin-top: 16px;
  border: 1px solid #ddd;
`;

export const TableHeader = styled.thead`
  background-color: #007bff;
  color: white;
  
  th {
    padding: 10px;
    text-align: left;
  }
`;

export const TableBody = styled.tbody`
  td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
`;