from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }




class Usuario(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    guardar = relationship("Guardar", back_populates="usuario")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }




class Planetas(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    planeta: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    n_guardados: Mapped[str] = mapped_column(nullable=False)

    id_guardar = mapped_column(ForeignKey("guardar.id"))
    guardar = relationship("Guardar", back_populates="planetas")

    def serialize(self):
        return {
            "id": self.id,
            "planeta": self.planeta,
            "guardados": self.n_guardados,
            # do not serialize the password, its a security breach
        }




class Personajes(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    personajes: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    id_guardar = mapped_column(ForeignKey("guardar.id"))
    guardar = relationship("Guardar", back_populates="personajes")

    def serialize(self):
        return {
            "id": self.id,
            "personajes": self.personajes,
            # do not serialize the password, its a security breach
        }




class Guardar(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_personajes: Mapped[int] = mapped_column(primary_key=True)
    id_planetas: Mapped[int] = mapped_column(primary_key=True)
 
    id_usuario = mapped_column(ForeignKey("usuario.id"))
    personajes = relationship("Personajes", back_populates="guardar")
    planetas = relationship("Planetas", back_populates="guardar")

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }