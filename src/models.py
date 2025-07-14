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

    favoritos = relationship("Favoritos", back_populates="usuario")

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

    favoritos = relationship("Favoritos", back_populates="planetas")

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
    favoritos_id = mapped_column(ForeignKey("favoritos.id"))

    favoritos = relationship("Favoritos", back_populates="personajes")

    def serialize(self):
        return {
            "id": self.id,
            "personajes": self.personajes,
            # do not serialize the password, its a security breach
        }




class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(primary_key=True)
    id_planetas: Mapped[int] = mapped_column(primary_key=True)
    id_personajes: Mapped[int] = mapped_column(primary_key=True)

    usuario = relationship("Usuario", back_populates="favoritos")
    personajes = relationship("Personajes", back_populates="favorito")
    planetas = relationship("Planetas", back_populates="favorito")

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta": self.planeta.serialize() if self.planeta else None,
            "personaje": self.personaje.serialize() if self.personaje else None
            # do not serialize the password, its a security breach
        }

