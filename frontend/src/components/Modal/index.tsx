import { ModalOverlay, ModalContent } from "./styles";
import { ReactNode } from "react";
import { useTheme } from "../../contexts/ThemeContext";

interface ModalProps {
    title: string;
    children: ReactNode;
    onClose: () => any;
}

const Modal = ({ title, children, onClose }: ModalProps) => {
    const { theme } = useTheme();

    return (
        <ModalOverlay onClick={onClose}>
            <ModalContent theme={theme} onClick={(e) => e.stopPropagation()}>
                <div className="modal-header">
                    <h1>{title}</h1>
                    <button className="close-btn" onClick={onClose}>
                        &times;
                    </button>
                </div>
                <div className="modal-body">{children}</div>
                <div className="modal-footer">
                    <button type="submit" onClick={() => console.log("save")}>Save</button>
                </div>
            </ModalContent>
        </ModalOverlay>
    );
};

export default Modal;